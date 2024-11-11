import pytest
import os
from dotenv import load_dotenv
from src.presentation.grpc.handler.route_guide_server import RouteGuideServicer
from tests.factories.route_factory import RouteFactory

@pytest.fixture
def route_guide_server():
    return RouteGuideServicer()

@pytest.fixture
def create_route(**kwargs):
    return RouteFactory(**kwargs)