from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from typing import Annotated, Optional
import asyncio
import httpx


app = FastAPI()


class Question(BaseModel):
    message: str
    callback_url: str


async def process_with_llm(message: str) -> str:
    response = f"Ответ от LLM на сообщение: {message}"
    return response


async def send_response(callback_url: str, response_data: dict):
    async with httpx.AsyncClient() as client:
        try:
            await client.post(callback_url, json=response_data)
        except httpx.HTTPError as e:
            print(f"Ошибка при отправке ответа: {e}")


@app.post("/webhook")
async def webhook_endpoint(question: Annotated[Question, Depends()]):
    try:
        llm_response = await process_with_llm(question.message)

        response_data = {"response": llm_response}

        await asyncio.create_task(send_response(question.callback_url, response_data))

        return {"status": "Webhook received, processing response"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
