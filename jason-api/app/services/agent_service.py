import requests


AGENT_URL = "http://127.0.0.1:8001/chat"


class AgentService:

    def send_message(self, messages: list[dict]) -> str:

        try:
            response = requests.post(
                AGENT_URL,
                json={
                    "messages": messages
                },
                timeout=300
            )

            response.raise_for_status()

            data = response.json()

            content = data.get("content", "").strip()

            if not content:
                raise RuntimeError(
                    "O JASON Agent retornou uma resposta vazia."
                )

            return content

        except requests.exceptions.ConnectionError:
            raise RuntimeError(
                "Não foi possível conectar ao JASON Agent."
            )

        except requests.exceptions.Timeout:
            raise RuntimeError(
                "O JASON Agent demorou demais para responder."
            )

        except requests.exceptions.RequestException as error:
            raise RuntimeError(
                f"Erro ao comunicar com o JASON Agent: {error}"
            )

        except (KeyError, ValueError):
            raise RuntimeError(
                "Resposta inválida recebida do JASON Agent."
            )
