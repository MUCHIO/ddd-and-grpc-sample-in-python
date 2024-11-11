from src.auto_generated.grpc import route_guide_pb2


def test_get_feature(create_route, route_guide_server):
    # Arrange
    request = route_guide_pb2.Point(
        latitude=create_route.latitude, longitude=create_route.longitude
    )

    # Act
    route = route_guide_server.GetFeature(request, None)

    # Assert
    assert route.name == create_route.name
