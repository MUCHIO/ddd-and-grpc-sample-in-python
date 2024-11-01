from typing import List, Optional
from src.infrastructure.database.schemas.route import Route
from src.domain.entities.route import RouteModel

class IRouteRepository:
    def create_route(self, route: RouteModel) -> RouteModel:
        raise NotImplementedError

    def find_route(self, route_id: int) -> Optional[RouteModel]:
        raise NotImplementedError

    def find_route_by_point(self, latitude: int, longitude: int) -> Optional[RouteModel]:
        raise NotImplementedError

    def update_route(self, route_id: int, updated_route: RouteModel) -> Optional[RouteModel]:
        raise NotImplementedError

    def delete_route(self, route_id: int) -> bool:
        raise NotImplementedError

    def list_routes(self) -> List[RouteModel]:
        raise NotImplementedError