import httpx

from schemas import Order

def fetch_order(order_id: str) -> Order | None:
    with httpx.Client(
        base_url = "http://127.0.0.1:8000",
        timeout = 5.0,
    ) as client:
        response = client.get(f"/mock/orders/{order_id}")

    if response.status_code == 404:
        return None

    response.raise_for_status()

    return Order.model_validate(response.json())