import pytest
from src.presentation.grpc.handler.route_guide_server import RouteGuideServicer
from tests.factories.route_factory import RouteFactory
from src.infrastructure.database.schemas.route import Base
from src.infrastructure.database import engine

@pytest.fixture
def route_guide_server():
    return RouteGuideServicer()

@pytest.fixture
def create_route(**kwargs):
    return RouteFactory(**kwargs)

@pytest.fixture(scope='session', autouse=True)
def setup_database():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    yield