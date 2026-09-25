from dataclasses import dataclass
from datetime import datetime
from movex_domain.enums.driver_status import DriverStatus


@dataclass
class Driver:
    user_id: int
    status: DriverStatus
    created_at: datetime
    updated_at: datetime
    deleted_at: datetime | None = None
