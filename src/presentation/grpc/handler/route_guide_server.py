# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Modified by MUCHIO on 2024-10-22
# Changes: Modified imported source package
# Modified by MUCHIO on 2024-10-31
# Changes: Replace DB from json to mysql
# Modified by MUCHIO on 2024-11-01
# Changes: Export some codes into src/application/services/route_summarize_application_service.py

"""The Python implementation of the gRPC route guide server."""

from concurrent import futures
import logging

import grpc
# import sys
# sys.path.append('/Users/hn/Documents/dev/workspace_github/ddd-and-grpc-sample-in-python/src')
from src.presentation.grpc.serializers.feature_serializer import FeatureSerializer
from src.presentation.grpc.serializers.route_summary_serializer import RouteSummarySerializer
from src.auto_generated.grpc import route_guide_pb2
from src.auto_generated.grpc import route_guide_pb2_grpc
from src.infrastructure.database import Session
from src.infrastructure.database.repositories.route_repository import RouteRepository
from src.application.services.route_summary_application_service import RouteSummaryApplicationService

def get_feature(route_repository, point):
    """Returns Feature at given location or None."""
    for route in route_repository.list_routes():
        if route.latitude == point.latitude and route.longitude == point.longitude:
            return route
    return None

class RouteGuideServicer(route_guide_pb2_grpc.RouteGuideServicer):
    """Provides methods that implement functionality of route guide server."""

    def GetFeature(self, request, context):
        self.route_repository = RouteRepository(Session())
        feature = get_feature(self.route_repository, request)
        if feature is None:
            return route_guide_pb2.Feature(name="", location=request)
        else:
            return FeatureSerializer.to_proto(feature)

    def ListFeatures(self, request, context):
        self.route_repository = RouteRepository(Session())
        left = min(request.lo.longitude, request.hi.longitude)
        right = max(request.lo.longitude, request.hi.longitude)
        top = max(request.lo.latitude, request.hi.latitude)
        bottom = min(request.lo.latitude, request.hi.latitude)
        for feature in self.route_repository.list_routes():
            if (
                feature.longitude >= left
                and feature.longitude <= right
                and feature.latitude >= bottom
                and feature.latitude <= top
            ):
                yield FeatureSerializer.to_proto(feature)

    def RecordRoute(self, request_iterator, context):
        route_summary = RouteSummaryApplicationService().summarize_route(request_iterator)
        return RouteSummarySerializer().to_proto(route_summary)

    def RouteChat(self, request_iterator, context):
        self.route_repository = RouteRepository(Session())
        prev_notes = []
        for new_note in request_iterator:
            for prev_note in prev_notes:
                if prev_note.location == new_note.location:
                    yield prev_note
            prev_notes.append(new_note)


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    route_guide_pb2_grpc.add_RouteGuideServicer_to_server(
        RouteGuideServicer(), server
    )
    server.add_insecure_port("[::]:50051")
    server.start()
    server.wait_for_termination()


if __name__ == "__main__":
    logging.basicConfig()
    serve()
