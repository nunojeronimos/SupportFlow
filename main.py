from fastapi import FastAPI
from typing import Annotated
from pydantic import BaseModel, StringConstraints
from mock_orders import router as mock_orders_router

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

@app.post("/requests")
def create_request(payload: SupportResquestInput) -> dict[str, str]:
    return {"message": payload.message}