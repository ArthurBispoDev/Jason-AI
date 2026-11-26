from fastapi import FastAPI
from app.routes.conversations import router as conversations_router

app = FastAPI(
    title="JASON API",
    description="Backend principal do JASON AI",
    version="2.0.0"
)

app.include_router(conversations_router)

@app.get("/")
def root():
    return {
        "message": "JASON API is running!",
        "version": "2.0.0"
    }
