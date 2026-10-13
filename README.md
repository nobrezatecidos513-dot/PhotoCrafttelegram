# PhotoCrafttelegram

Bot do Telegram para edição de fotos diretamente no chat, com filtros profissionais, menu interativo e suporte opcional a doações.

## Visão geral

O PhotoCrafttelegram permite que o usuário envie uma imagem e escolha filtros para aplicar no Telegram, recebendo o resultado imediatamente no chat.

## Funcionalidades

- envio de fotos no Telegram
- menu interativo com filtros
- edição de imagens com Pillow
- filtros: Preto & Branco, Sépia, Contraste, Vintage, Warm, Sharpen, Brilho, Frio, Suave e Marca d'água
- comando /donate para apoio opcional
- ambiente pronto para execução local

## Como configurar

Crie um arquivo `.env` na raiz do projeto com:

```env
BOT_TOKEN=SEU_TOKEN_DO_BOT
DONATE_TON_ADDRESS=UQDfIXVzruwv_nqmpK6L7nsKGfUb_8pGqLJ9_cHZleH6mDbd
DONATE_KOFI=
DONATE_PAYPAL=
DONATE_GITHUB=
```

## Instalação

```bash
pip install -r requirements.txt
python bot.py
```

## Comandos do bot

- /start — mensagem inicial
- /help — explica como usar
- /menu — abre o menu de filtros
- /donate — mostra opções de apoio opcional

## Observações

- A doação é totalmente opcional.
- O bot funciona normalmente sem doação.
- O endereço TON pode ser trocado por qualquer outra carteira de sua preferência.

## Stack

- Python
- aiogram
- Pillow
- python-dotenv

## Repositório

https://github.com/nobrezatecidos513-dot/PhotoCrafttelegram
