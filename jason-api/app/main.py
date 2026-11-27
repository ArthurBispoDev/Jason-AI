from fastapi import FastAPI
from app.routes.conversations import router as conversations_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="JASON API",
    description="Backend principal do JASON AI",
    version="2.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:4200",
        "http://127.0.0.1:4200"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(conversations_router)

@app.get("/")
def root():
    return {
        "message": "JASON API is running!",
        "version": "2.0.0"
    }


