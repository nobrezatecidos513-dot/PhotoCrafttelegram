# PhotoCrafttelegram

Versão 3 do bot do Telegram para edição de fotos com filtros interativos e processamento profissional no próprio chat.

## O que mudou na versão 3

- menu de filtros mais completo
- suporte a efeitos: Preto & Branco, Sépia, Contraste, Vintage, Warm, Sharp
- feedback visual mais profissional
- melhor organização da lógica do bot
- tratamento de erros e mensagens de ajuda mais claras

## Como funciona

1. O usuário envia uma foto para o bot.
2. O bot mostra os filtros disponíveis.
3. O usuário escolhe um efeito.
4. O bot aplica o filtro e devolve a imagem editada como resposta.

## Tecnologias

- Python
- aiogram
- Pillow

## Como executar

1. Crie um bot no Telegram usando o @BotFather.
2. Copie o token do bot.
3. Crie um arquivo `.env` com o conteúdo abaixo:

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
- `/menu` — mostra os filtros disponíveis

## Observação

Esta é uma versão mais robusta do projeto, funcionando diretamente dentro do Telegram como um bot de edição de fotos.
