# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: file_uploader.proto
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
    'file_uploader.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.rpc import status_pb2 as google_dot_rpc_dot_status__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x66ile_uploader.proto\x12\tmypackage\x1a\x17google/rpc/status.proto\"\x1e\n\x08\x46ileData\x12\x12\n\x04\x64\x61ta\x18\x01 \x01(\x0cR\x04\x64\x61ta2C\n\x0c\x46ileUploader\x12\x33\n\x08SendFile\x12\x13.mypackage.FileData\x1a\x12.google.rpc.StatusBf\n\rcom.mypackageB\x11\x46ileUploaderProtoP\x01\xa2\x02\x03MXX\xaa\x02\tMypackage\xca\x02\tMypackage\xe2\x02\x15Mypackage\\GPBMetadata\xea\x02\tMypackageb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'file_uploader_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  _globals['DESCRIPTOR']._loaded_options = None
  _globals['DESCRIPTOR']._serialized_options = b'\n\rcom.mypackageB\021FileUploaderProtoP\001\242\002\003MXX\252\002\tMypackage\312\002\tMypackage\342\002\025Mypackage\\GPBMetadata\352\002\tMypackage'
  _globals['_FILEDATA']._serialized_start=59
  _globals['_FILEDATA']._serialized_end=89
  _globals['_FILEUPLOADER']._serialized_start=91
  _globals['_FILEUPLOADER']._serialized_end=158
# @@protoc_insertion_point(module_scope)
