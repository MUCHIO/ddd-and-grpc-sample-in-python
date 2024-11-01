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

# Modified by MUCHIO on 2024-11-01
# Changes: Imported from src/presentation/grpc/handler/route_guide_server.py


import time, math
from src.infrastructure.database.repositories.route_repository import RouteRepository
from src.infrastructure.database import Session
from src.auto_generated.grpc import route_guide_pb2
from src.application.dto.route_summary_dto import RouteSummaryDTO

class RouteSummaryApplicationService:
    def __init__(self):
        self.route_repository = RouteRepository(Session())

    def summarize_route(self, request_iterator) -> route_guide_pb2.RouteSummary:
        point_count = 0
        feature_count = 0
        distance = 0.0
        prev_point = None

        start_time = time.time()
        for point in request_iterator:
            point_count += 1
            if self.get_feature(self.route_repository, point):
                feature_count += 1
            if prev_point:
                distance += self.get_distance(prev_point, point)
            prev_point = point

        elapsed_time = time.time() - start_time
        return RouteSummaryDTO(
            point_count=point_count,
            feature_count=feature_count,
            distance=int(distance),
            elapsed_time=int(elapsed_time),
        )

    # Duplicate code from src/presentation/grpc/handler/route_guide_server.py
    def get_feature(self, route_repository, point):
        """Returns Feature at given location or None."""
        for route in route_repository.list_routes():
            if route.latitude == point.latitude and route.longitude == point.longitude:
                return route
        return None

    def get_distance(self, start, end):
        """Distance between two points."""
        coord_factor = 10000000.0
        lat_1 = start.latitude / coord_factor
        lat_2 = end.latitude / coord_factor
        lon_1 = start.longitude / coord_factor
        lon_2 = end.longitude / coord_factor
        lat_rad_1 = math.radians(lat_1)
        lat_rad_2 = math.radians(lat_2)
        delta_lat_rad = math.radians(lat_2 - lat_1)
        delta_lon_rad = math.radians(lon_2 - lon_1)

        # Formula is based on http://mathforum.org/library/drmath/view/51879.html
        a = pow(math.sin(delta_lat_rad / 2), 2) + (
            math.cos(lat_rad_1)
            * math.cos(lat_rad_2)
            * pow(math.sin(delta_lon_rad / 2), 2)
        )
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        R = 6371000
        # metres
        return R * c