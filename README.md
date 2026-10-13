# PhotoCrafttelegram

Versão 5 do bot do Telegram para edição de fotos com filtros profissionais, marca d'água e melhor experiência de uso.

## O que mudou na versão 5

- filtros mais completos
- integração de marca d'água e brilho
- feedback visual mais profissional
- menu interativo melhorado
- estrutura do bot organizada para fácil manutenção
- suporte a doação opcional via TON (Gram) e outras opções de apoio

## Funcionalidades

- envio de fotos diretamente no Telegram
- escolha de filtro em menu interativo
- edição de imagem com Pillow
- retorno da foto editada no chat
- opção de texto de marca d'água na imagem
- comando `/donate` para apoiar o projeto de forma opcional

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
   DONATE_TON_ADDRESS=SEU_ENDERECO_TON
   DONATE_KOFI=
   DONATE_PAYPAL=
   DONATE_GITHUB=
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
- `/menu` — mostra filtros
- `/donate` — mostra opções de apoio voluntário

## Observação

Esta versão é um bot funcionando dentro do aplicativo do Telegram, ideal para edição de fotos diretamente no chat. O apoio é totalmente opcional.
