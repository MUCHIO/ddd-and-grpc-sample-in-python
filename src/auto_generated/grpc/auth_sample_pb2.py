# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: auth_sample.proto
# Protobuf Python Version: 5.27.2
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    27,
    2,
    '',
    'auth_sample.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x61uth_sample.proto\x12\x0cgrpc.testing\":\n\x07Request\x12\x15\n\rfill_username\x18\x04 \x01(\x08\x12\x18\n\x10\x66ill_oauth_scope\x18\x05 \x01(\x08\"1\n\x08Response\x12\x10\n\x08username\x18\x02 \x01(\t\x12\x13\n\x0boauth_scope\x18\x03 \x01(\t2I\n\x0bTestService\x12:\n\tUnaryCall\x12\x15.grpc.testing.Request\x1a\x16.grpc.testing.ResponseB\x07\xa2\x02\x04\x41UTHb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'auth_sample_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\242\002\004AUTH'
  _globals['_REQUEST']._serialized_start=35
  _globals['_REQUEST']._serialized_end=93
  _globals['_RESPONSE']._serialized_start=95
  _globals['_RESPONSE']._serialized_end=144
  _globals['_TESTSERVICE']._serialized_start=146
  _globals['_TESTSERVICE']._serialized_end=219
# @@protoc_insertion_point(module_scope)
