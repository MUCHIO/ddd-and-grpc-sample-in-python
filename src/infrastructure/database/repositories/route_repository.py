from typing import List, Optional
from sqlalchemy import select
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
        stmt = select(Route).where(Route.id == route_id)
        result = self.session.execute(stmt).scalar_one_or_none()
        if result:
            return RouteModel.model_validate(result)
        return None

    def find_route_by_point(self, latitude: int, longitude: int) -> RouteModel | None:
        stmt = select(Route).where(
            Route.latitude == latitude,
            Route.longitude == longitude
        )
        result = self.session.execute(stmt).scalar_one_or_none()
        if result:
            return RouteModel.model_validate(result)
        return None

    def update_route(self, route_id: int, updated_route: RouteModel) -> Optional[RouteModel]:
        stmt = select(Route).where(Route.id == route_id)
        result = self.session.execute(stmt).first()
        if result:
            for key, value in updated_route.dict().items():
                setattr(result, key, value)
            self.session.commit()
            self.session.refresh(result)
            return RouteModel.model_validate(result)
        return None

    def delete_route(self, route_id: int) -> bool:
        stmt = select(Route).where(Route.id == route_id)
        result = self.session.execute(stmt).scalar_one_or_none()
        if result:
            self.session.delete(result)
            self.session.commit()
            return True
        return False

    def list_routes(self) -> List[RouteModel]:
        stmt = select(Route)
        results = self.session.execute(stmt).scalars().all()
        return [RouteModel.model_validate(route) for route in results]