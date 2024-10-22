from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class Request(_message.Message):
    __slots__ = ("fill_username", "fill_oauth_scope")
    FILL_USERNAME_FIELD_NUMBER: _ClassVar[int]
    FILL_OAUTH_SCOPE_FIELD_NUMBER: _ClassVar[int]
    fill_username: bool
    fill_oauth_scope: bool
    def __init__(self, fill_username: bool = ..., fill_oauth_scope: bool = ...) -> None: ...

class Response(_message.Message):
    __slots__ = ("username", "oauth_scope")
    USERNAME_FIELD_NUMBER: _ClassVar[int]
    OAUTH_SCOPE_FIELD_NUMBER: _ClassVar[int]
    username: str
    oauth_scope: str
    def __init__(self, username: _Optional[str] = ..., oauth_scope: _Optional[str] = ...) -> None: ...
