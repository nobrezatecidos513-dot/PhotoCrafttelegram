# PhotoCrafttelegram

Versão 2 do bot do Telegram para processar fotos com filtros e devolver a imagem editada no próprio chat.

## O que mudou na versão 2

- menu com filtros interativos
- opções de edição: Preto & Branco, Sépia, Contraste e Vintage
- envio de imagem com resposta em linha no Telegram
- melhor experiência para usuários que enviam fotos diretamente para o bot

## Como funciona

- O usuário envia uma foto para o bot.
- O bot mostra opções de filtros.
- O usuário escolhe um efeito.
- O bot retorna a imagem com o filtro aplicado.

## Tecnologias

- Python
- aiogram
- Pillow

## Como executar

1. Crie um bot no Telegram usando o @BotFather.
2. Copie o token do bot.
3. Crie um arquivo `.env` com o seguinte conteúdo:

   ```env
   BOT_TOKEN=SEU_TOKEN_AQUI
   ```

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
- `/menu` — mostra opções de filtro

## Observação

Esta é uma versão mais completa do projeto, funcionando diretamente dentro do aplicativo Telegram como um bot de processamento de imagem.
