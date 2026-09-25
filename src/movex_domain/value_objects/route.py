from dataclasses import dataclass
from movex_domain.value_objects.geo_point import GeoPoint


@dataclass(frozen=True)
class Route:
    distance_meters: float
    duration_seconds: float
    geometry: list[GeoPoint]
    waypoints: list[GeoPoint]
