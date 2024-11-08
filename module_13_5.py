from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
import asyncio
 
BOT_TOKEN = "токен из Botfather" 

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage()) 

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'], state='*')
async def cmd_start(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = types.KeyboardButton("Рассчитать")
    button_info = types.KeyboardButton("Информация") 
    keyboard.add(button_calculate, button_info)
    await message.reply("Привет! Давай посчитаем твою норму калорий.", reply_markup=keyboard)
    await state.finish()


@dp.message_handler(text='Рассчитать', state=None) 
async def set_age(message: types.Message, state: FSMContext):
    await message.reply("Введите свой возраст:")
    await UserState.age.set()


async def main():
    await dp.start_polling()

if __name__ == '__main__':
    asyncio.run(main())

@dp.message_handler(text='Информация', state='*')
async def send_info(message: types.Message):
    await message.reply("Этот бот поможет вам рассчитать вашу суточную норму калорий.  Вам потребуется ввести ваш возраст, рост и вес.")


