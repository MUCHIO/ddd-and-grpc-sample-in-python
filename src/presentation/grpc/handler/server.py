
import grpc
from concurrent import futures
from src.auto_generated.grpc import route_guide_pb2_grpc
from src.presentation.grpc.handler.route_guide_server import RouteGuideServicer
from src.presentation.grpc.interceptors.logging_interceptor import LoggingInterceptor
from src.presentation.grpc.interceptors.jwt_Interceptor import JwtInterceptor

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10), interceptors=[LoggingInterceptor(), JwtInterceptor()])
    route_guide_pb2_grpc.add_RouteGuideServicer_to_server(RouteGuideServicer(), server)
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    serve()