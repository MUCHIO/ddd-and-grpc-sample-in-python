import grpc
import jwt
from config.config import settings

class JwtInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        metadata = dict(handler_call_details.invocation_metadata)
        token = metadata.get('authorization')
        print(token)
        if not token:
            context = grpc.ServicerContext()
            context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Authorization token is missing')

        try:
            # JWTトークンを検証
            payload = jwt.decode(token, settings.secret_key, algorithms=['HS256'])
            if metadata.get('user_id') != payload['user_id']:
                context = grpc.ServicerContext()
                context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Invalid user_id')
        except jwt.ExpiredSignatureError:
            context = grpc.ServicerContext()
            context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Token has expired')
        except jwt.InvalidTokenError:
            context = grpc.ServicerContext()
            context.abort(grpc.StatusCode.UNAUTHENTICATED, 'Invalid token')

        return continuation(handler_call_details)