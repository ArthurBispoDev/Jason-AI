import requests

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Literal

from config.system_prompt import SYSTEM_PROMPT


app = FastAPI(
    title="JASON Agent",
    description="Serviço de inteligência do JASON",
    version="2.0.0"
)

OLLAMA_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3.5:9b"


class MessageInput(BaseModel): # Mensagem enviada
    role: Literal["user", "assistant"]
    content: str


class ChatRequest(BaseModel): # Histórico de mensagens
    messages: list[MessageInput]


class ChatResponse(BaseModel): # Resposta do Jason
    content: str


@app.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):

    # Adiciono o System Prompt antes do histórico
    messages = [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        }
    ]

    messages.extend(
        message.model_dump()
        for message in request.messages
    )

    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": MODEL,
                "messages": messages,
                "stream": False,
                "think": False,
                "options": {
                    "temperature": 0.5,
                    "top_p": 0.9,
                    "top_k": 20
                }
            },
            timeout=300
        )

        response.raise_for_status()

        data = response.json()

        message = data.get("message", {})
        content = message.get("content", "").strip()

        if not content:
            thinking = message.get("thinking", "")

            print("\n[ERRO] Ollama retornou conteúdo vazio.")
            print(f"Modelo: {data.get('model')}")
            print(f"Motivo do término: {data.get('done_reason')}")
            print(f"Tamanho do thinking: {len(thinking)}")

            raise HTTPException(
                status_code=502,
                detail="O Ollama retornou uma resposta sem conteúdo."
            )

        return ChatResponse(content=content)

    except requests.exceptions.RequestException as error:
        raise HTTPException(
            status_code=502,
            detail=f"Erro ao comunicar com o Ollama: {error}"
        )

    except (KeyError, ValueError):
        raise HTTPException(
            status_code=502,
            detail="Resposta inválida recebida do Ollama."
        )
