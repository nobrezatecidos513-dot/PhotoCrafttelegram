import os
from io import BytesIO

from PIL import Image, ImageDraw
from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters import Command
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN não foi encontrado. Crie um arquivo .env com o seu token do Telegram.")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Bem-vindo ao PhotoCraft Telegram!\n\n"
        "Envie uma foto para aplicar um efeito simples.\n"
        "Comandos disponíveis:\n"
        "/start - iniciar\n"
        "/help - ajuda"
    )


@dp.message_handler(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        "Como usar:\n"
        "1. Envie uma foto para o bot\n"
        "2. O bot aplica um efeito simples de edição\n"
        "3. Receba a imagem editada de volta"
    )


@dp.message_handler(content_types=['photo'])
async def handle_photo(message: types.Message):
    photo = message.photo[-1]
    file = await bot.get_file(photo.file_id)
    file_bytes = await bot.download_file(file.file_path)

    img = Image.open(BytesIO(file_bytes)).convert("RGB")
    width, height = img.size

    result = img.copy()
    draw = ImageDraw.Draw(result)

    draw.rectangle((0, height - 120, width, height), fill=(0, 0, 0, 180))
    draw.text((20, height - 90), "PhotoCraft", fill=(255, 255, 255))
    draw.rounded_rectangle((20, 20, width - 20, 90), radius=15, fill=(255, 255, 255, 80))

    output = BytesIO()
    result.save(output, format="JPEG", quality=90)
    output.seek(0)

    await message.answer_photo(
        types.InputFile(output, filename="photo_craft.jpg"),
        caption="✨ Foto processada pelo PhotoCraft Telegram"
    )


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
