from dataclasses import dataclass
from datetime import datetime
from movex_domain.enums.notification_type import NotificationType


@dataclass
class Notification:
    id: int
    user_id: int
    title: str
    message: str
    is_read: bool
    created_at: datetime
