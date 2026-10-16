from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Literal
from datetime import date
from schemas import Order


router = APIRouter(prefix = "/mock", tags = ["Mock orders"])



ORDERS = {
    "ORD-1001": Order(
        order_id = "ORD-1001",
        status = "shipped",
        estimated_delivery = date(2026, 10, 20),
    ),
    "ORD-1002": Order(
        order_id = "ORD-1002",
        status = "delivered",
    ),
}

@router.get("/orders/{order_id}", response_model = Order)
def get_order(order_id: str) -> Order:
    order = ORDERS.get(order_id)

    if order is None:
        raise HTTPException(
            status_code = 404,
            detail = "Order not found",
        )

    return order