import os
import asyncio
from aiogram import Bot, Dispatcher, types, F

# Читаем переменные окружения с Railway
TOKEN = os.getenv("TOKEN")
GAME_SHORT_NAME = os.getenv("GAME_SHORT_NAME")
GAME_URL = os.getenv("GAME_URL")

# Проверяем, что все переменные заданы
if not TOKEN:
    raise ValueError("❌ Переменная TOKEN не найдена! Добавь её в Variables Railway.")
if not GAME_SHORT_NAME:
    raise ValueError("❌ Переменная GAME_SHORT_NAME не найдена!")
if not GAME_URL:
    raise ValueError("❌ Переменная GAME_URL не найдена!")

# Создаём бота и диспетчер
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(F.text == "/start")
async def start_game(message: types.Message):
    await message.answer_game(GAME_SHORT_NAME)

# Обработчик нажатия на кнопку игры
@dp.callback_query(F.game_short_name == GAME_SHORT_NAME)
async def game_callback(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id, url=GAME_URL)

# Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
