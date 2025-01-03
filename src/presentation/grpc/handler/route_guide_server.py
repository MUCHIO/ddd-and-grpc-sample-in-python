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
# Changes: Implement Application Service
# Changes: Add logging config and interceptors
# Modified by MUCHIO on 2024-12-03
# Changes: Add JwtInterceptor and logger


"""The Python implementation of the gRPC route guide server."""

from logging import getLogger, FileHandler, DEBUG, Formatter

import grpc
from src.presentation.grpc.serializers.feature_serializer import FeatureSerializer
from src.presentation.grpc.serializers.route_summary_serializer import RouteSummarySerializer
from src.auto_generated.grpc import route_guide_pb2
from src.auto_generated.grpc import route_guide_pb2_grpc
from src.infrastructure.database.repositories.route_repository import RouteRepository
from src.application.services.route_summary_application_service import RouteSummaryApplicationService
from src.application.services.feature_application_service import FeatureApplicationService
from src.infrastructure.database import session_scope
from config.config import settings

logger = getLogger(__name__)
logger.setLevel(DEBUG)
handler = FileHandler('grpc_server.log')
handler.setLevel(DEBUG)
formatter = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.propagate = False

class RouteGuideServicer(route_guide_pb2_grpc.RouteGuideServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self, database_url):
        self.database_url = database_url

    def GetFeature(self, request, context):
        # メタデータからuser_idを取得
        metadata = dict(context.invocation_metadata())
        user_id = metadata.get('user_id')
        if user_id:
            logger.debug(f"User ID: {user_id}")

        with session_scope(self.database_url) as session:
            feature = FeatureApplicationService(session).find_feature_by_point(request.latitude, request.longitude)
            if feature is None:
                return route_guide_pb2.Feature(name="", location=request)
            else:
                return FeatureSerializer.to_proto(feature)

    def ListFeatures(self, request, context):
        with session_scope(self.database_url) as session:
            left = min(request.lo.longitude, request.hi.longitude)
            right = max(request.lo.longitude, request.hi.longitude)
            top = max(request.lo.latitude, request.hi.latitude)
            bottom = min(request.lo.latitude, request.hi.latitude)
            for feature in FeatureApplicationService(session).find_feature_in_rectangle(left, right, top, bottom):
                yield FeatureSerializer().to_proto(feature)

    def RecordRoute(self, request_iterator, context):
        with session_scope(self.database_url) as session:
            route_summary = RouteSummaryApplicationService(session).summarize_route(request_iterator)
            return RouteSummarySerializer().to_proto(route_summary)

    def RouteChat(self, request_iterator, context):
        with session_scope(self.database_url) as session:
            self.route_repository = RouteRepository(session)
            prev_notes = []
            for new_note in request_iterator:
                for prev_note in prev_notes:
                    if prev_note.location == new_note.location:
                        yield prev_note
                prev_notes.append(new_note)
