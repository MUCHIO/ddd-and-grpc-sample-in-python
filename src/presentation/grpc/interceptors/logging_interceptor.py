from grpc import ServerInterceptor
from logging import getLogger, StreamHandler, DEBUG

class LoggingInterceptor(ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        method_name = handler_call_details.method
        logger = getLogger(__name__)
        logger.info("Request for {} method starts.".format(method_name))

        # リクエストを処理する
        response = continuation(handler_call_details)

        logger.info("Request for {} method ends.".format(method_name))
        return response