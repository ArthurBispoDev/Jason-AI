import requests
from config.system_prompt import SYSTEM_PROMPT

API_URL = "http://localhost:11434/api/chat"
MODEL = "qwen3.5:4b"

user_name = "Você"
bot_name = "JASON"

# Histórico de conversas
messages = []

# Adicionando o System Prompt
messages.append({
    "role": "system",
    "content": SYSTEM_PROMPT
})

print(f"{bot_name} iniciado!")
print("Digite '/bye' para encerrar.\nDigite '/messages' para ver o histórico de mensagens")

while True:

    # Recebe a mensagem do usuário
    user_input = input(f"{user_name}: ")

    if user_input.lower().strip() == "/bye":
        print(f"{bot_name}: Até logo!")
        break

    if user_input.lower().strip() == "/messages":
        print(messages)
        continue

    # Adiciona a mensagem ao histórico
    messages.append({
        "role": "user",
        "content": user_input
    })

    try:

        # Envia a requisição ao Ollama
        response = requests.post(
            API_URL,
            json={
                "model": MODEL,
                "messages": messages, # Envio todo histórico a cada mensagem, incluindo a atual
                "stream": False
            },
            timeout=300
        )

        response.raise_for_status()

        # Converte a resposta para JSON
        data = response.json()

        # Extrai o conteúdo da resposta
        assistant_response = data["message"]["content"]

        print(f"\n{bot_name}: {assistant_response}\n") # Envio o contéudo inteiro no chat

        # Adiciono a resposta no histórico de mensagens
        messages.append({
            "role": "assistant",
            "content": assistant_response
        })

    except requests.exceptions.ConnectionError:
        print("\nErro: Não foi possível conectar ao Ollama.")
        print("Verifique se o Ollama está em execução.\n")

    except requests.exceptions.RequestException as error:
        print(f"\nErro na requisição: {error}\n")
