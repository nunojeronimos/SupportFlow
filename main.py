from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel, StringConstraints
from mock_orders import router as mock_orders_router
from triage_service import process_request
from schemas import ProcessRequest

app = FastAPI(
    title = "SupportFlow",
    description = "AI-assisted customer support triage.",
    version = "0.1.0"
)

app.include_router(mock_orders_router)

class SupportResquestInput(BaseModel):
    message: Annotated[
        str,
        StringConstraints(
            strip_whitespace = True,
            min_length = 1,
            max_length = 5000
        )
    ]

@app.get("/health")
def healt_check() -> dict[str, str]:
    return {"status": "ok"}

@app.post("/requests", response_model = ProcessRequest)
def create_request(payload: SupportResquestInput) -> ProcessRequest:
    return process_request(payload.message)