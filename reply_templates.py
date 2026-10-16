from schemas import Order, TriageResult


def build_suggestes_reply(analysis: TriageResult, reason_code: str, order: Order | None,) -> str:
    if reason_code == "MISSING_ORDER_ID":
        return "Could you please provide your order number?"

    if reason_code == "ORDER_NOT_FOUND":
        return (
            "We could not find that order. "
            "Please check the order number so our support team can assist."
        )

    if reason_code == "ORDER_LOOKUP_FAILED":
        return (
            "We could not check your ordder status at this time. "
            "Please try again later."
        )

    if reason_code == "ORDER_FOUND" and order is not None:
        if analysis.category == "return_request":
            return (
                f"Your return request for order {order.order_id}"
                "requires review by our support team. "
                "This does not confirm approval of the return"
            )

        status_messages = {
            "processing": "is being processed",
            "shipped": "has shipped",
            "delivered": "is marked as delivered",
            "cancelled": "is marked as cancelled",
        }

        reply = (
            f"Your order {order.order_id} "
            f"{status_messages[order.status]}."
        )

        if (order.status in {"processing", "shipped"} and order.estimated_delivery is not None):
            reply += (
                f" Estimated delivery: "
                f"{order.estimated_delivery.isoformat()}."
            )

        return reply

    return "Your message requires review by our support team."