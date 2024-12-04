from src.auto_generated.grpc import route_guide_pb2


def test_get_feature(mocker, create_route, route_guide_server):
    # Arrange
    request = route_guide_pb2.Point(
        latitude=create_route.latitude, longitude=create_route.longitude
    )

    # Create a mock context with invocation_metadata method
    context = mocker.Mock()
    context.invocation_metadata.return_value = []

    # Act
    route = route_guide_server.GetFeature(request, context)

    # Assert
    assert route.name == create_route.name
