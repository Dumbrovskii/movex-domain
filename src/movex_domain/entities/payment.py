from dataclasses import dataclass
from datetime import datetime
from decimal import Decimal
from movex_domain.enums.payment_status import PaymentStatus


@dataclass
class Payment:
    id: int
    ride_id: int
    amount: Decimal
    currency: str
    status: PaymentStatus
    transaction_id: str
    created_at: datetime
    updated_at: datetime
