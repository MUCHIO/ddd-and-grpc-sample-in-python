from typing import List, Optional
from sqlalchemy.orm import Session
from src.infrastructure.database.schemas.route import Route
from src.domain.entities.route import RouteModel
from src.domain.repository_interfaces.route_repository_interface import IRouteRepository
from src.infrastructure.database import session_scope

class RouteRepository(IRouteRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_route(self, route: RouteModel) -> RouteModel:
        db_route = Route(**route.dict())
        self.session.add(db_route)
        self.session.commit()
        self.session.refresh(db_route)
        return RouteModel.model_validate(db_route)

    def find_route(self, route_id: int) -> Optional[RouteModel]:
        db_route = self.session.query(Route).filter(Route.id == route_id).first()
        if db_route:
            return RouteModel.model_validate(db_route)
        return None

    def find_route_by_point(self, latitude: int, longitude: int) -> RouteModel | None:
        db_route = self.session.query(Route).filter(Route.latitude == latitude, Route.longitude == longitude).first()
        if db_route:
            return RouteModel.model_validate(db_route)
        return None

    def update_route(self, route_id: int, updated_route: RouteModel) -> Optional[RouteModel]:
        db_route = self.session.query(Route).filter(Route.id == route_id).first()
        if db_route:
            for key, value in updated_route.dict().items():
                setattr(db_route, key, value)
            self.session.commit()
            self.session.refresh(db_route)
            return RouteModel.model_validate(db_route)
        return None

    def delete_route(self, route_id: int) -> bool:
        db_route = self.session.query(Route).filter(Route.id == route_id).first()
        if db_route:
            self.session.delete(db_route)
            self.session.commit()
            return True
        return False

    def list_routes(self) -> List[RouteModel]:
        db_routes = self.session.query(Route).all()
        return [RouteModel.model_validate(route) for route in db_routes]