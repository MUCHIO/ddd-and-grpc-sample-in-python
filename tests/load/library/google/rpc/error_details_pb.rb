# frozen_string_literal: true
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: google/rpc/error_details.proto

require 'google/protobuf'

require 'google/protobuf/duration_pb'


descriptor_data = "\n\x1egoogle/rpc/error_details.proto\x12\ngoogle.rpc\x1a\x1egoogle/protobuf/duration.proto\"\xb9\x01\n\tErrorInfo\x12\x16\n\x06reason\x18\x01 \x01(\tR\x06reason\x12\x16\n\x06\x64omain\x18\x02 \x01(\tR\x06\x64omain\x12?\n\x08metadata\x18\x03 \x03(\x0b\x32#.google.rpc.ErrorInfo.MetadataEntryR\x08metadata\x1a;\n\rMetadataEntry\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\x12\x14\n\x05value\x18\x02 \x01(\tR\x05value:\x02\x38\x01\"G\n\tRetryInfo\x12:\n\x0bretry_delay\x18\x01 \x01(\x0b\x32\x19.google.protobuf.DurationR\nretryDelay\"H\n\tDebugInfo\x12#\n\rstack_entries\x18\x01 \x03(\tR\x0cstackEntries\x12\x16\n\x06\x64\x65tail\x18\x02 \x01(\tR\x06\x64\x65tail\"\x9b\x01\n\x0cQuotaFailure\x12\x42\n\nviolations\x18\x01 \x03(\x0b\x32\".google.rpc.QuotaFailure.ViolationR\nviolations\x1aG\n\tViolation\x12\x18\n\x07subject\x18\x01 \x01(\tR\x07subject\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\"\xbd\x01\n\x13PreconditionFailure\x12I\n\nviolations\x18\x01 \x03(\x0b\x32).google.rpc.PreconditionFailure.ViolationR\nviolations\x1a[\n\tViolation\x12\x12\n\x04type\x18\x01 \x01(\tR\x04type\x12\x18\n\x07subject\x18\x02 \x01(\tR\x07subject\x12 \n\x0b\x64\x65scription\x18\x03 \x01(\tR\x0b\x64\x65scription\"\x8c\x02\n\nBadRequest\x12P\n\x10\x66ield_violations\x18\x01 \x03(\x0b\x32%.google.rpc.BadRequest.FieldViolationR\x0f\x66ieldViolations\x1a\xab\x01\n\x0e\x46ieldViolation\x12\x14\n\x05\x66ield\x18\x01 \x01(\tR\x05\x66ield\x12 \n\x0b\x64\x65scription\x18\x02 \x01(\tR\x0b\x64\x65scription\x12\x16\n\x06reason\x18\x03 \x01(\tR\x06reason\x12I\n\x11localized_message\x18\x04 \x01(\x0b\x32\x1c.google.rpc.LocalizedMessageR\x10localizedMessage\"O\n\x0bRequestInfo\x12\x1d\n\nrequest_id\x18\x01 \x01(\tR\trequestId\x12!\n\x0cserving_data\x18\x02 \x01(\tR\x0bservingData\"\x90\x01\n\x0cResourceInfo\x12#\n\rresource_type\x18\x01 \x01(\tR\x0cresourceType\x12#\n\rresource_name\x18\x02 \x01(\tR\x0cresourceName\x12\x14\n\x05owner\x18\x03 \x01(\tR\x05owner\x12 \n\x0b\x64\x65scription\x18\x04 \x01(\tR\x0b\x64\x65scription\"o\n\x04Help\x12+\n\x05links\x18\x01 \x03(\x0b\x32\x15.google.rpc.Help.LinkR\x05links\x1a:\n\x04Link\x12 \n\x0b\x64\x65scription\x18\x01 \x01(\tR\x0b\x64\x65scription\x12\x10\n\x03url\x18\x02 \x01(\tR\x03url\"D\n\x10LocalizedMessage\x12\x16\n\x06locale\x18\x01 \x01(\tR\x06locale\x12\x18\n\x07message\x18\x02 \x01(\tR\x07messageB\xad\x01\n\x0e\x63om.google.rpcB\x11\x45rrorDetailsProtoP\x01Z?google.golang.org/genproto/googleapis/rpc/errdetails;errdetails\xa2\x02\x03GRX\xaa\x02\nGoogle.Rpc\xca\x02\nGoogle\\Rpc\xe2\x02\x16Google\\Rpc\\GPBMetadata\xea\x02\x0bGoogle::Rpcb\x06proto3"

pool = Google::Protobuf::DescriptorPool.generated_pool
pool.add_serialized_file(descriptor_data)

module Google
  module Rpc
    ErrorInfo = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("google.rpc.ErrorInfo").msgclass
    RetryInfo = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("google.rpc.RetryInfo").msgclass
    DebugInfo = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("google.rpc.DebugInfo").msgclass
    QuotaFailure = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("google.rpc.QuotaFailure").msgclass
    QuotaFailure::Violation = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("google.rpc.QuotaFailure.Violation").msgclass
    PreconditionFailure = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("google.rpc.PreconditionFailure").msgclass
    PreconditionFailure::Violation = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("google.rpc.PreconditionFailure.Violation").msgclass
    BadRequest = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("google.rpc.BadRequest").msgclass
    BadRequest::FieldViolation = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("google.rpc.BadRequest.FieldViolation").msgclass
    RequestInfo = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("google.rpc.RequestInfo").msgclass
    ResourceInfo = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("google.rpc.ResourceInfo").msgclass
    Help = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("google.rpc.Help").msgclass
    Help::Link = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("google.rpc.Help.Link").msgclass
    LocalizedMessage = ::Google::Protobuf::DescriptorPool.generated_pool.lookup("google.rpc.LocalizedMessage").msgclass
  end
end