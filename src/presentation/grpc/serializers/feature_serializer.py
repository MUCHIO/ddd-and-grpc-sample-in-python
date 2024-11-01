from src.application.dto.route_dto import RouteDTO
from src.auto_generated.grpc.route_guide_pb2 import Feature, Point

class FeatureSerializer:
    @staticmethod
    def to_proto(route: RouteDTO) -> Feature:
        return Feature(
            name=route.name,
            location=Point(
                latitude=route.latitude,
                longitude=route.longitude,
            ),
        )