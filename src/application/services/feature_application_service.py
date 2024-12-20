from typing import Generator, Optional
from src.infrastructure.database.repositories.route_repository import RouteRepository
from src.application.dto.route_dto import RouteDTO
from src.infrastructure.database import session_scope
from sqlalchemy.orm import Session

class FeatureApplicationService:
    def __init__(self, session: Session):
        self.route_repository = RouteRepository(session)

    def find_feature_by_point(self, latitude: int, longitude: int) -> Optional[RouteDTO]:
        return self.route_repository.find_route_by_point(latitude, longitude)

    def find_feature_in_rectangle(self, left: int, right: int, top:int, bottom: int) -> Generator[RouteDTO, None, None]:
        for feature in self.route_repository.list_routes():
            if (
                feature.longitude >= left
                and feature.longitude <= right
                and feature.latitude >= bottom
                and feature.latitude <= top
            ):
                yield RouteDTO(
                    name=feature.name,
                    latitude=feature.latitude,
                    longitude=feature.longitude,
                )
