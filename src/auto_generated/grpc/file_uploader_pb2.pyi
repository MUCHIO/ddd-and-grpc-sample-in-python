from google.rpc import status_pb2 as _status_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class FileData(_message.Message):
    __slots__ = ("liked_song_feature_vectors", "disliked_song_feature_vectors")
    LIKED_SONG_FEATURE_VECTORS_FIELD_NUMBER: _ClassVar[int]
    DISLIKED_SONG_FEATURE_VECTORS_FIELD_NUMBER: _ClassVar[int]
    liked_song_feature_vectors: _containers.RepeatedScalarFieldContainer[bytes]
    disliked_song_feature_vectors: _containers.RepeatedScalarFieldContainer[bytes]
    def __init__(self, liked_song_feature_vectors: _Optional[_Iterable[bytes]] = ..., disliked_song_feature_vectors: _Optional[_Iterable[bytes]] = ...) -> None: ...
