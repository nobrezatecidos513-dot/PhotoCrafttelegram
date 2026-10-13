# PhotoCrafttelegram

Versão 4 do bot do Telegram para edição de fotos com filtros profissionais, marca d'água e melhor experiência de uso.

## O que mudou na versão 4

- filtros mais completos
- suporte a brilho, frio, sharpen e marca d'água
- melhor organização do código do bot
- experiência mais profissional com mensagens de confirmação e ajuda

## Funcionalidades

- envio de fotos diretamente no Telegram
- escolha de filtro em menu interativo
- processamento de imagem com Pillow
- retorno da foto editada no chat

## Tecnologias

- Python
- aiogram
- Pillow

## Como executar

1. Crie um bot usando o @BotFather.
2. Copie o token do bot.
3. Crie um arquivo `.env` com:

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
- `/help` — ajuda
- `/menu` — mostra filtros

## Observação

Esta é uma versão mais avançada do projeto, funcionando diretamente dentro do aplicativo do Telegram como um bot de processamento de imagem.
