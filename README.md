# PhotoCrafttelegram

Bot do Telegram para processar fotos com efeitos simples e devolver a imagem editada dentro do próprio Telegram.

## Como funciona

- O usuário envia uma foto para o bot.
- O bot processa a imagem com Pillow.
- O bot devolve uma imagem com efeito visual simples.

## Tecnologias

- Python
- aiogram
- Pillow

## Como executar

1. Crie um bot no Telegram usando o @BotFather.
2. Copie o token do bot.
3. Crie um arquivo `.env` com o conteúdo do exemplo:

   `BOT_TOKEN=SEU_TOKEN_AQUI`

4. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

5. Inicie o bot:

   ```bash
   python bot.py
   ```

## Comandos

- `/start` — inicia o bot
- `/help` — mostra instruções de uso

## Observação

Este projeto foi estruturado como um bot do Telegram dentro do próprio aplicativo, seguindo o nome e a ideia inicial do repositório.
