# frozen_string_literal: true
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: file_uploader.proto

require 'google/protobuf'

require 'google/rpc/status_pb'


descriptor_data = "\n\x13\x66ile_uploader.proto\x12\tmypackage\x1a\x17google/rpc/status.proto\"\x1e\n\x08\x46ileData\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta2C\n\x0c\x46ileUploader\x12\x33\n\x08SendFile\x12\x13.mypackage.FileData\x1a\x12.google.rpc.StatusBf\n\rcom.mypackageB\x11\x46ileUploaderProtoP\x01\xa2\x02\x03MXX\xaa\x02\tMypackage\xca\x02\tMypackage\xe2\x02\x15Mypackage\\GPBMetadata\xea\x02\tMypackageb\x06proto3"

pool = Google::Protobuf::DescriptorPool.generated_pool
pool.add_serialized_file(descriptor_data)

module Mypackage
  FileData = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("mypackage.FileData").msgclass
end
