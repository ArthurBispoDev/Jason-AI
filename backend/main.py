import requests

from backend.config.system_prompt import SYSTEM_PROMPT

import json
from backend.database.repository import create_conversation, save_message


API_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3.5:4b"

user_name = "\033[33mVocê\033[0m"
bot_name = "\033[34mJASON\033[0m"

# Histórico de conversas
messages = []
conversation_id = None

# Adicionando o System Prompt
messages.append({
    "role": "system",
    "content": SYSTEM_PROMPT
})

print(f"{bot_name} iniciado!")
print("\033[32mDigite '/bye' para encerrar.\nDigite '/messages' para ver o histórico de mensagens\033[0m")

while True:

    # Recebe a mensagem do usuário
    user_input = input(f"{user_name}: ")

    if user_input.lower().strip() == "/bye":
        print(f"{bot_name}: Até logo!")
        break

    if user_input.lower().strip() == "/messages":
        print(messages)
        continue

    # Adiciona a mensagem ao histórico temporário
    messages.append({
        "role": "user",
        "content": user_input
    })

    # Cria uma conversa ou salva a mensagem nela
    if conversation_id is None:
        conversation_id = create_conversation(user_input)
    else:
        save_message(conversation_id, "user", user_input)

    try:

        # Envia a requisição ao Ollama
        response = requests.post(
            API_URL,
            json={
                "model": MODEL,
                "messages": messages,
                "stream": True,
                "think": False,
                "options": {
                    "temperature": 0.75 # > mais criativo, < mais técnico
                }
            },
            stream=True,
            timeout=300
        )

        response.raise_for_status()

        assistant_response = ""

        print(f"\n{bot_name}: ", end="", flush=True)


        # Adiciono aos poucos cada pedaço para dar efeito de digitação em tempo real
        for line in response.iter_lines():

            if line:

                data = json.loads(line)

                content = data["message"]["content"]

                if content:
                    assistant_response += content
                    print(content, end="", flush=True)

        # Pulo linha no fim da resposta
        print("\n")

        # Adiciono a resposta no histórico de mensagens
        messages.append({
            "role": "assistant",
            "content": assistant_response
        })

        # Salvo a resposta dele na conversa
        save_message(conversation_id, "assistant", assistant_response)

    except requests.exceptions.ConnectionError:
        print("\nErro: Não foi possível conectar ao Ollama.")
        print("Verifique se o Ollama está em execução.\n")

    except requests.exceptions.RequestException as error:
        print(f"\nErro na requisição: {error}\n")
