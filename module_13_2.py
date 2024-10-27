import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

API_TOKEN = 'Токен из Botfather' 

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    print('Привет! Я бот, помогающий твоему здоровью.')
    await message.reply('Привет! Я здесь, чтобы помочь тебе. Напиши что-то или используй команду /start.')

@dp.message_handler()
async def all_messages(message: types.Message):
    print('Введите команду /start, чтобы начать общение.')
    await message.reply('Эта команда не распознана. Попробуйте /start.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)