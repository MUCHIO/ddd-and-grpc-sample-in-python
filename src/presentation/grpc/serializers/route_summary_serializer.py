from src.application.dto.route_summary_dto import RouteSummaryDTO
from src.auto_generated.grpc.route_guide_pb2 import RouteSummary

class RouteSummarySerializer:
    @staticmethod
    def to_proto(route_summary_dto: RouteSummaryDTO) -> RouteSummary:
        return RouteSummary(
            point_count=route_summary_dto.point_count,
            feature_count=route_summary_dto.feature_count,
            distance=int(route_summary_dto.distance),
            elapsed_time=int(route_summary_dto.elapsed_time),
        )