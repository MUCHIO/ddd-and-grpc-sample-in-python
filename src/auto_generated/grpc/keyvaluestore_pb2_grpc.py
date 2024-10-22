# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
import warnings

import keyvaluestore_pb2 as keyvaluestore__pb2

GRPC_GENERATED_VERSION = '1.67.0'
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower
    _version_not_supported = first_version_is_lower(GRPC_VERSION, GRPC_GENERATED_VERSION)
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f'The grpc package installed is at version {GRPC_VERSION},'
        + f' but the generated code in keyvaluestore_pb2_grpc.py depends on'
        + f' grpcio>={GRPC_GENERATED_VERSION}.'
        + f' Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}'
        + f' or downgrade your generated code using grpcio-tools<={GRPC_VERSION}.'
    )


class KeyValueStoreStub(object):
    """A simple key-value storage service
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetValues = channel.stream_stream(
                '/keyvaluestore.KeyValueStore/GetValues',
                request_serializer=keyvaluestore__pb2.Request.SerializeToString,
                response_deserializer=keyvaluestore__pb2.Response.FromString,
                _registered_method=True)


class KeyValueStoreServicer(object):
    """A simple key-value storage service
    """

    def GetValues(self, request_iterator, context):
        """Provides a value for each key request
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_KeyValueStoreServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetValues': grpc.stream_stream_rpc_method_handler(
                    servicer.GetValues,
                    request_deserializer=keyvaluestore__pb2.Request.FromString,
                    response_serializer=keyvaluestore__pb2.Response.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'keyvaluestore.KeyValueStore', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers('keyvaluestore.KeyValueStore', rpc_method_handlers)


 # This class is part of an EXPERIMENTAL API.
class KeyValueStore(object):
    """A simple key-value storage service
    """

    @staticmethod
    def GetValues(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(
            request_iterator,
            target,
            '/keyvaluestore.KeyValueStore/GetValues',
            keyvaluestore__pb2.Request.SerializeToString,
            keyvaluestore__pb2.Response.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True)
