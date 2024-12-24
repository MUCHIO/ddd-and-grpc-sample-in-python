this_dir = File.expand_path(File.dirname(__FILE__))
lib_dir = File.join(this_dir, 'library')
$LOAD_PATH.unshift(lib_dir) unless $LOAD_PATH.include?(lib_dir)

require 'grpc'
require 'file_uploader_services_pb'
require 'dotenv'
require 'jwt'

include Fileuploader

def generate_jwt_token(user_id)
  payload = { 'user_id' => user_id }
  token = JWT.encode(payload, ENV['SECRET_KEY'], 'HS256')
  token
end

def run_file_upload(stub, liked_feature_file_paths, disliked_feature_file_paths, metadata)
  p 'FileUpload'
  p '----------'
  
  # ファイルを読み込んでバイナリデータとして送信
  liked_feature_files = liked_feature_file_paths.map do |liked_feature_file_path| IO.binread(liked_feature_file_path) end
  disliked_feature_files = disliked_feature_file_paths.map do |disliked_feature_file_path| IO.binread(disliked_feature_file_path) end
  request = FileData.new(
    liked_song_feature_vectors: liked_feature_files,
    disliked_song_feature_vectors: disliked_feature_files
  )

  response = stub.send_file(request, metadata: metadata)
  p "File uploaded status: #{response.message}"
rescue GRPC::BadStatus => e
  puts "エラーコード: #{e.code}"
  puts "エラー詳細: #{e.details}"
end

def main(liked_feature_file_path_1 = nil,liked_feature_file_path_2 = nil,liked_feature_file_path_3 = nil, disliked_feature_file_path_4 = nil,disliked_feature_file_path_5 = nil,disliked_feature_file_path_6 = nil)
  Dotenv.load '.env.ruby'

  liked_feature_file_paths = [liked_feature_file_path_1, liked_feature_file_path_2, liked_feature_file_path_3]
  disliked_feature_file_paths = [disliked_feature_file_path_4, disliked_feature_file_path_5, disliked_feature_file_path_6]
  (liked_feature_file_paths + disliked_feature_file_paths).flatten.each do |feature_file_path|
    puts feature_file_path
    if feature_file_path.nil?
      puts "Usage: ruby file_uploader_client.rb <liked_feature_file_path> <liked_feature_file_path> <liked_feature_file_path> <disliked_feature_file_path> <disliked_feature_file_path> <disliked_feature_file_path>"
      exit 1
    elsif !File.exist?(feature_file_path)
      puts "#{feature_file_path} does not exist."
      exit 1
    end
  end

  stub = FileUploader::Stub.new("#{ENV['GRPC_SERVER']}:#{ENV['GRPC_PORT']}", :this_channel_is_insecure)
  token = generate_jwt_token('user123')
  metadata = { 'authorization' => token, 'user_id' => 'user123' }
  run_file_upload(stub, liked_feature_file_paths, disliked_feature_file_paths, metadata)
end
