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

    def __init__(self, database_url):
        self.database_url = database_url

    def SendFile(self, request, context):
        try:
            for liked_song_feature_vector in request.liked_song_feature_vectors:
                with open('uploaded_file', 'wb') as f:
                    logger.debug(liked_song_feature_vector)
            for disliked_song_feature_vector in request.disliked_song_feature_vectors:
                with open('uploaded_file', 'wb') as f:
                    logger.debug(disliked_song_feature_vector)
            return status_pb2.Status(code=0, message="Success")
        except Exception as e:
            return status_pb2.Status(code=1, message=str(e))
