from src.auto_generated.grpc import route_guide_pb2
from src.application.services.feature_application_service import FeatureApplicationService
from src.presentation.grpc.serializers.feature_serializer import FeatureSerializer

def test_get_feature_found(mocker, route_guide_server):
    # Arrange
    request = route_guide_pb2.Point(latitude=409146138, longitude=-746188906)
    name = 'Patriots Path, Mendham, NJ, USA'
    route_dto_mock = mocker.patch('src.application.dto.route_dto.RouteDTO')
    route_dto_mock.name = name
    mocker.patch.object(FeatureApplicationService, 'find_feature_by_point', return_value=route_dto_mock)
    mocker.patch.object(FeatureSerializer, 'to_proto', return_value=route_guide_pb2.Feature(name=route_dto_mock.name, location=request))

    # Create a mock context with invocation_metadata method
    context = mocker.Mock()
    context.invocation_metadata.return_value = []

    # Act
    response = route_guide_server.GetFeature(request, context)

    # Assert
    assert response.name == name
    FeatureApplicationService.find_feature_by_point.assert_called_once_with(request.latitude, request.longitude)
    FeatureSerializer.to_proto.assert_called_once_with(route_dto_mock)

def test_get_feature_not_found(mocker, route_guide_server):
    # Arrange
    request = route_guide_pb2.Point(latitude=409146138, longitude=-746188906)
    mocker.patch.object(FeatureApplicationService, 'find_feature_by_point', return_value=None)

    # Create a mock context with invocation_metadata method
    context = mocker.Mock()
    context.invocation_metadata.return_value = []

    # Act
    response = route_guide_server.GetFeature(request, context)

    # Assert
    assert response.name == ''
    assert response.location == request
    FeatureApplicationService.find_feature_by_point.assert_called_once_with(request.latitude, request.longitude)