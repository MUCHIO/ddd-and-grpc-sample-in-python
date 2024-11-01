from src.domain.entities.route import RouteModel
from src.auto_generated.grpc.route_guide_pb2 import Feature, Point

class FeatureSerializer:
    @staticmethod
    def to_proto(route: RouteModel) -> Feature:
        return Feature(
            name=route.name,
            location=Point(
                latitude=route.latitude,
                longitude=route.longitude,
            ),
        )