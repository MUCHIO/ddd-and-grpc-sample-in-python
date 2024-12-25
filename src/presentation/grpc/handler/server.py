
import grpc
from concurrent import futures
from src.auto_generated.grpc import route_guide_pb2_grpc, file_uploader_pb2_grpc
from src.presentation.grpc.handler.route_guide_server import RouteGuideServicer
from src.presentation.grpc.handler.file_uploader import FileUploader
from src.presentation.grpc.interceptors.logging_interceptor import LoggingInterceptor
from src.presentation.grpc.interceptors.jwt_Interceptor import JwtInterceptor
from config.config import settings

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=[LoggingInterceptor(), JwtInterceptor()])
    file_uploader_pb2_grpc.add_FileUploaderServicer_to_server(FileUploader(settings.database_url), server)
    route_guide_pb2_grpc.add_RouteGuideServicer_to_server(RouteGuideServicer(settings.database_url), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()