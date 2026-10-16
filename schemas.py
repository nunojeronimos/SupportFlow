from typing import Literal
from pydantic import BaseModel, Field
from datetime import date


class TriageResult(BaseModel):
    category: Literal["delivery_status", "return_request", "other"]
    summary: str = Field(min_length = 1, max_length = 500)
    order_id: str | None

class Order(BaseModel):
    order_id: str
    status: Literal["processing", "shipped", "delivered", "cancelled"]
    estimated_delivery: date | None = None

class ProcessRequest(TriageResult):
    processing_status: Literal[
        "ready_for_review",
        "needs_information",
        "manual_review",
        "processing_error",
    ]
    reason_code: str
    order: Order | None = None
    suggested_reply: str