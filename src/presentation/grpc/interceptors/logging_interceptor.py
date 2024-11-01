from grpc import ServerInterceptor
import logging

class LoggingInterceptor(ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        method_name = handler_call_details.method
        print(f"Received request for method: {method_name}")
        logging.debug(f"Received request for method: {method_name}")

        # リクエストを処理する
        response = continuation(handler_call_details)

        return response