#!/usr/bin/env ruby

# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Sample app that connects to a Route Guide service.
#
# Usage: $ path/to/route_guide_client.rb path/to/route_guide_db.json &

# Modified by MUCHIO on 2024-11-14
# Changes: lib_dir path and dir name
# Modified by MUCHIO on 2024-11-15
# Changes: comment main
# Modified by MUCHIO on 2024-11-29
# Changes: Made grpc server host and port configurable
# Modified by MUCHIO on 2024-12-03
# Changes: Added JWT token generation

this_dir = File.expand_path(File.dirname(__FILE__))
lib_dir = File.join(this_dir, 'library')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'grpc'
require 'multi_json'
require 'route_guide_services_pb'
require 'dotenv'
require 'jwt'

include Routeguide

GET_FEATURE_POINTS = [
  Point.new(latitude:  409_146_138, longitude: -746_188_906),
  Point.new(latitude:  0, longitude: 0)
]

# JWTトークンを生成
def generate_jwt_token(user_id)
  payload = { 'user_id' => user_id }
  token = JWT.encode(payload, ENV['SECRET_KEY'], 'HS256')
  token
end

# runs a GetFeature rpc.
#
# - once with a point known to be present in the sample route database
# - once with a point that is not in the sample database
def run_get_feature(stub, metadata)
  p 'GetFeature'
  p '----------'
  GET_FEATURE_POINTS.each do |pt|
    resp = stub.get_feature(pt, metadata: metadata)
    if resp.name != ''
      p "- found '#{resp.name}' at #{pt.inspect}"
    else
      p "- found nothing at #{pt.inspect}"
    end
    rescue GRPC::BadStatus => e
      puts "エラーコード: #{e.code}"
      puts "エラー詳細: #{e.details}"
  end
end

LIST_FEATURES_RECT = Rectangle.new(
  lo: Point.new(latitude: 400_000_000, longitude: -750_000_000),
  hi: Point.new(latitude: 420_000_000, longitude: -730_000_000))

# runs a ListFeatures rpc.
#
# - the rectangle to chosen to include most of the known features
#   in the sample db.
def run_list_features(stub, metadata)
  p 'ListFeatures'
  p '------------'
  resps = stub.list_features(LIST_FEATURES_RECT, metadata: metadata)
  resps.each do |r|
    p "- found '#{r.name}' at #{r.location.inspect}"
  end
end

# RandomRoute provides an Enumerable that yields a random 'route' of points
# from a list of Features.
class RandomRoute
  def initialize(features, size)
    @features = features
    @size = size
  end

  # yields a point, waiting between 0 and 1 seconds between each yield
  #
  # @return an Enumerable that yields a random point
  def each
    return enum_for(:each) unless block_given?
    @size.times do
      json_feature = @features[rand(0..@features.length)]
      next if json_feature.nil?
      location = json_feature['location']
      pt = Point.new(
        Hash[location.each_pair.map { |k, v| [k.to_sym, v] }])
      p "- next point is #{pt.inspect}"
      yield pt
      sleep(rand(0..1))
    end
  end
end

# runs a RecordRoute rpc.
#
# - the rectangle to chosen to include most of the known features
#   in the sample db.
def run_record_route(stub, features, metadata)
  p 'RecordRoute'
  p '-----------'
  points_on_route = 10  # arbitrary
  reqs = RandomRoute.new(features, points_on_route)
  resp = stub.record_route(reqs.each, metadata: metadata)
  p "summary: #{resp.inspect}"
end

ROUTE_CHAT_NOTES = [
  RouteNote.new(message: 'doh - a deer',
                location: Point.new(latitude: 0, longitude: 0)),
  RouteNote.new(message: 'ray - a drop of golden sun',
                location: Point.new(latitude: 0, longitude: 1)),
  RouteNote.new(message: 'me - the name I call myself',
                location: Point.new(latitude: 1, longitude: 0)),
  RouteNote.new(message: 'fa - a longer way to run',
                location: Point.new(latitude: 1, longitude: 1)),
  RouteNote.new(message: 'soh - with needle and a thread',
                location: Point.new(latitude: 0, longitude: 1))
]

# runs a RouteChat rpc.
#
# sends a canned set of route notes and prints out the responses.
def run_route_chat(stub, metadata)
  p 'Route Chat'
  p '----------'
  sleeping_enumerator = SleepingEnumerator.new(ROUTE_CHAT_NOTES, 1)
  stub.route_chat(sleeping_enumerator.each_item, metadata: metadata) { |r| p "received #{r.inspect}" }
end

# SleepingEnumerator yields through items, and sleeps between each one
class SleepingEnumerator
  def initialize(items, delay)
    @items = items
    @delay = delay
  end
  def each_item
    return enum_for(:each_item) unless block_given?
    @items.each do |item|
      sleep @delay
      p "next item to send is #{item.inspect}"
      yield item
    end
  end
end

def main(json = nil)
  Dotenv.load '.env.ruby'

  stub = RouteGuide::Stub.new("#{ENV['GRPC_SERVER']}:#{ENV['GRPC_PORT']}", :this_channel_is_insecure)
  token = generate_jwt_token('user123')
  metadata = { 'authorization' => token, 'user_id' => 'user123' }
  run_get_feature(stub, metadata)
  run_list_features(stub, metadata)
  run_route_chat(stub, metadata)
  unless json
    p 'no feature database; skipping record_route'
    exit
  end
  raw_data = []
  File.open(json) do |f|
    raw_data = MultiJson.load(f.read)
  end
  run_record_route(stub, raw_data, metadata)
end