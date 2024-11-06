from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import aiogram.dispatcher.filters.state 
import State, StatesGroup
from aiogram.dispatcher import FSMContext
import asyncio
BOT_TOKEN = "ключ из BotFather"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'], state='*')
async def cmd_start(message: types.Message, state: FSMContext):
    await message.reply("Привет! Давай посчитаем твою норму калорий. Напиши 'Calories'")
    await state.finish()


@dp.message_handler(text='Calories', state=None)
async def set_age(message: types.Message, state: FSMContext):
    await message.reply("Введите свой возраст:")
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.reply("Введите свой рост (в см):")
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message: types.Message, state: FSMContext):
    await state.update_data(growth=message.text)
    await message.reply("Введите свой вес (в кг):")
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message: types.Message, state: FSMContext):
    await state.update_data(weight=message.text)
    data = await state.get_data()
    age = int(data['age'])
    growth = int(data['growth'])
    weight = float(data['weight'])

    calories = 655 + (9.6 * weight) + (1.85 * growth) - (4.7 * age)

    await message.reply(f"Ваша приблизительная норма калорий: {calories:.0f} ккал")
    await state.finish()
async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
