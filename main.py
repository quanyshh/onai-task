from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Annotated, Optional

app = FastAPI()


class Question(BaseModel):
    message: str
    callback_url: str


@app.post("/webhook")
async def webhook_endpoint(question: Annotated[Question, Depends()]):
    try:
        return {"status": "Webhook received, processing response"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
