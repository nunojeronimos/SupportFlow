from schemas import TriageResult

def analyze_message(message: str) -> TriageResult:
    """Return fixed results for development examples."""
    examples = {
        "My order ORD-1001 has not arrived. Can you check its status?": {
            "category": "delivery_status",
            "summary": "Customer asks about a delayed order.",
            "order_id": "ORD-1001",
        },
        "I want to return my purchase.": {
            "category": "return_request",
            "summary": "Customer wants to return a purchase.",
            "order_id": None,
        },
    }

    result = examples.get(message)

    if result is None:
        return TriageResult(
            category = "other",
            summary = "Message is outside the configured mock examples.",
            order_id = None,
        )

    return TriageResult(**result)