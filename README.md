# Jason AI

## Ferramentas
### Linguagens e FrameWorks
- Python 3.14.19
- Angular 22.2.1

### Modelos de IA e Ambientes Utilizados
- Qwen 3.5 4B
- Ollama 0.40.17

### Banco de dados
- PostGreSQL 4

### Bibliotecas
Python (pip install)
- requests

## Versão do Jason
Jason 2.0 BETA
Estado: Em desenvolvimento


## Requisitos do Sistema

### Hardware

| Componente | Mínimo estimado | Recomendado |
|---|---|---|
| Processador | Intel Core i5 / AMD Ryzen 5 | Intel Core i7 / AMD Ryzen 7 |
| Memória RAM | 8 GB | 16 GB ou superior |
| Placa de vídeo | Integrada (execução via CPU) | GPU dedicada com 8 GB VRAM |
| Armazenamento | 6 GB livres | 10 GB livres ou superior |

### Software

- Windows 10 ou Windows 11 (64 bits).
- Python 3.10 ou superior.
- Ollama instalado e configurado.
- Modelo Qwen 3.5 4B.

**Observações:**
- O modelo é executado localmente através do Ollama, sem necessidade de uma API comercial.
- A execução via CPU é possível, mas pode apresentar menor desempenho.
- Uma GPU compatível pode acelerar a geração das respostas.
- É necessária conexão com a internet para baixar o modelo inicialmente.


## Etapas de desenvolvimento
1. ChatBot simples
2. Histórico de mensagens temporárias
3. Personalidade e System Prompt
4. Histórico de mensagens com PostGreSQL
5. Tool Calling
6. Reconhecimento e síntese de voz
7. Interface DeskTop com Angular e Electron
8. Automação e controle do computador

## Comandos

Ollama:
- Adicionar o Qwen no Ollama:
    ollama pull qwen3.5:4b
- Inicializar o Qwen
    ollama run qwen3.5:4b
- Ver se está sendo rodado na CPU ou GPU
    ollama ps



