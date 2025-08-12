from aiogram import Bot, Dispatcher, types
import asyncio

TOKEN = "8343837798:AAFSRbHFKLGjA6l9mlQB9Nk1-62WfKmAToE"
GAME_SHORT_NAME = "vzlom_of_system"  # тот самый, что указывали в BotFather
GAME_URL = "https://minchc.github.io/Vzlom_oF_System/"  # ссылка на GitHub Pages

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start_game(message: types.Message):
    await message.answer_game(GAME_SHORT_NAME)

@dp.callback_query_handler(lambda c: c.game_short_name == GAME_SHORT_NAME)
async def game_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, url=GAME_URL)

async def main():
    await dp.start_polling()

asyncio.run(main())
