import httpx

from pydantic import ValidationError
from mock_analyser import analyze_message
from orders_client import fetch_order
from schemas import ProcessRequest
from reply_templates import build_suggestes_reply


def process_request(message: str) -> ProcessRequest:
    analysis = analyze_message(message)
    order = None

    if analysis.category == "other":
        status = "manual_review"
        reason = "UNSUPPORTED_OR_AMBIGUOUS_REQUEST"

    elif analysis.order_id is None:
        status = "needs_information"
        reason = "MISSING_ORDER_ID"

    else:
        try:
            order = fetch_order(analysis.order_id)

        except (httpx.HTTPError, ValidationError, ValueError):
            status = "processing_error"
            reason = "ORDER_LOOKUP_FAILED"

        else:
            if order is None:
                status = "manual_review"
                reason = "ORDER_NOT_FOUND"
            else:
                status = "ready_for_review"
                reason = "ORDER_FOUND"
    
    return ProcessRequest(
        **analysis.model_dump(),
        processing_status = status,
        reason_code = reason,
        order = order,
        suggested_reply = build_suggestes_reply(
            analysis = analysis,
            reason_code = reason,
            order = order
        ),
    )
