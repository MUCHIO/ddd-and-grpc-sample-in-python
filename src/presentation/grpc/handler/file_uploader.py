from logging import getLogger, FileHandler, DEBUG, Formatter
from src.auto_generated.grpc import file_uploader_pb2_grpc
from src.auto_generated.grpc.google.rpc import status_pb2

logger = getLogger(__name__)
logger.setLevel(DEBUG)
handler = FileHandler('grpc_server.log')
handler.setLevel(DEBUG)
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.propagate = False

class FileUploader(file_uploader_pb2_grpc.FileUploaderServicer):
    def SendFile(self, request, context):
        try:
            file_data = request.data
            with open('uploaded_file', 'wb') as f:
                logger.debug(file_data)
            return status_pb2.Status(code=0, message="Success")
        except Exception as e:
            return status_pb2.Status(code=1, message=str(e))
