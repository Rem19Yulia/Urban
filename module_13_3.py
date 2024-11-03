import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils import executor

api = "токен из BotFather" 

logging.basicConfig(level=logging.INFO)

bot = Bot(token=api)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply('Привет! Я бот, помогающий твоему здоровью.  Чем я могу тебе помочь?') 

@dp.message_handler(lambda message: True)
async def all_messages(message: types.Message): 
    await message.reply("Введите команду /start , чтобы начать общение.")


if __name__ == "__main__": 
    executor.start_polling(dp, skip_updates=True)