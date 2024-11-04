from fastapi import FastAPI, HTTPException, Request


app = FastAPI()


@app.post("/webhook")
async def webhook_endpoint(request: Request):
    try:
        return {"status": "Webhook received, processing response"}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
