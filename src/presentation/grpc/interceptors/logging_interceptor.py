from grpc import ServerInterceptor
from logging import getLogger, FileHandler, DEBUG, Formatter

# ロガーの設定を一度だけ行う
logger = getLogger(__name__)
logger.setLevel(DEBUG)
handler = FileHandler('grpc_server.log')
handler.setLevel(DEBUG)
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.propagate = False

class LoggingInterceptor(ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        method_name = handler_call_details.method
        
        # リクエストの開始をログに記録
        logger.info("Request for {} method starts.".format(method_name))

        # リクエストを処理する
        response = continuation(handler_call_details)

        # リクエストの終了をログに記録
        logger.info("Request for {} method ends.".format(method_name))
        
        return response