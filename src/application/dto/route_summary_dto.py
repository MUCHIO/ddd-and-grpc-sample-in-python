from dataclasses import dataclass

@dataclass
class RouteSummaryDTO:
    point_count: int
    feature_count: int
    distance: int
    elapsed_time: int