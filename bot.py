import os
import asyncio
from aiogram import Bot, Dispatcher, types, F

TOKEN = os.getenv("8343837798:AAFSRbHFKLGjA6l9mlQB9Nk1-62WfKmAToE")
GAME_SHORT_NAME = os.getenv("vzlom_of_system")
GAME_URL = os.getenv("https://minchc.github.io/Vzlom_oF_System/")

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(F.text == "/start")
async def start_game(message: types.Message):
    await message.answer_game(GAME_SHORT_NAME)

@dp.callback_query(F.game_short_name == GAME_SHORT_NAME)
async def game_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, url=GAME_URL)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
