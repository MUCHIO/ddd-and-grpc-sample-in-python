# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: keyvaluestore.proto
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
    'keyvaluestore.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13keyvaluestore.proto\x12\rkeyvaluestore\"\x1b\n\x07Request\x12\x10\n\x03key\x18\x01 \x01(\tR\x03key\" \n\x08Response\x12\x14\n\x05value\x18\x01 \x01(\tR\x05value2S\n\rKeyValueStore\x12\x42\n\tGetValues\x12\x16.keyvaluestore.Request\x1a\x17.keyvaluestore.Response\"\x00(\x01\x30\x01\x42{\n\x11\x63om.keyvaluestoreB\x12KeyvaluestoreProtoP\x01\xa2\x02\x03KXX\xaa\x02\rKeyvaluestore\xca\x02\rKeyvaluestore\xe2\x02\x19Keyvaluestore\\GPBMetadata\xea\x02\rKeyvaluestoreb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'keyvaluestore_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\021com.keyvaluestoreB\022KeyvaluestoreProtoP\001\242\002\003KXX\252\002\rKeyvaluestore\312\002\rKeyvaluestore\342\002\031Keyvaluestore\\GPBMetadata\352\002\rKeyvaluestore'
  _globals['_REQUEST']._serialized_start=38
  _globals['_REQUEST']._serialized_end=65
  _globals['_RESPONSE']._serialized_start=67
  _globals['_RESPONSE']._serialized_end=99
  _globals['_KEYVALUESTORE']._serialized_start=101
  _globals['_KEYVALUESTORE']._serialized_end=184
# @@protoc_insertion_point(module_scope)
