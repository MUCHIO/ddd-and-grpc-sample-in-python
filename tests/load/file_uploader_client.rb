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

def run_file_upload(stub, file_path, metadata)
  p 'FileUpload'
  p '----------'
  
  # ファイルを読み込んでバイナリデータとして送信
  file_content = IO.binread(file_path)
  request = FileData.new(
    data: file_content
  )
  
  response = stub.send_file(request, metadata: metadata)
  p "File uploaded successfully: #{response.message}"
rescue GRPC::BadStatus => e
  puts "エラーコード: #{e.code}"
  puts "エラー詳細: #{e.details}"
end

def main(file_path = nil)
  Dotenv.load '.env.ruby'

  if file_path.nil? || !File.exist?(file_path)
    puts "Usage: ruby file_uploader_client.rb <file_path>"
    exit 1
  end

  stub = FileUploader::Stub.new("#{ENV['GRPC_SERVER']}:#{ENV['GRPC_PORT']}", :this_channel_is_insecure)
  token = generate_jwt_token('user123')
  metadata = { 'authorization' => token, 'user_id' => 'user123' }
  run_file_upload(stub, file_path, metadata)
end

# main(ARGV[0])