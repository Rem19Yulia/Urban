from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import crud_functions#
import asyncio

BOT_TOKEN = "ключ доступа"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

# Инициируем базу данных и заполняем её, если это еще не сделано
crud_functions.initiate_db()
crud_functions.populate_db()
class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

@dp.message_handler(commands=['start'], state='*')
async def cmd_start(message: types.Message, state: FSMContext):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_calculate = types.KeyboardButton("Рассчитать")
    button_info = types.KeyboardButton("Информация")
    button_buy = types.KeyboardButton("Купить")
    keyboard.add(button_calculate, button_info, button_buy)
    await message.reply(f"Привет! Давай посчитаем твою норму калорий, {message.from_user.username} !", reply_markup=keyboard)
    await state.finish()


@dp.message_handler(text='Информация', state='*')
async def send_info(message: types.Message):
    await message.reply("Этот бот поможет вам рассчитать вашу суточную норму калорий. Вам потребуется ввести ваш возраст, рост и вес.")


@dp.message_handler(text='Рассчитать', state=None)
async def main_menu(message: types.Message):
    inline_keyboard = InlineKeyboardMarkup(row_width=1)
    button_calories = InlineKeyboardButton("Рассчитать норму калорий", callback_data='calories')
    button_formulas = InlineKeyboardButton("Формулы расчёта", callback_data='formulas')
    inline_keyboard.add(button_calories, button_formulas)
    await message.reply("Выберите опцию:", reply_markup=inline_keyboard)


@dp.callback_query_handler(lambda call: call.data == 'formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.message.answer("Формула Миффлина-Сан Жеора: (10 * вес в кг) + (6.25 * рост в см) - (5 * возраст в годах) + 5 (для мужчин) / -161 (для женщин)")
    await call.answer()


@dp.callback_query_handler(lambda call: call.data == 'calories', state=None)
async def set_age(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Введите свой возраст (число):")
    await UserState.age.set()
    await call.answer()


@dp.message_handler(state=UserState.age)
async def process_age(message: types.Message, state: FSMContext):
    try:
        age = int(message.text)
        if age < 0 or age > 120:
            await message.reply("Некорректный возраст. Пожалуйста, введите число от 0 до 120.")
            return
        await state.update_data(age=age)
        await message.reply("Введите свой рост в сантиметрах (число):")
        await UserState.next()
    except ValueError:
        await message.reply("Некорректный ввод. Пожалуйста, введите число.")


@dp.message_handler(state=UserState.growth)
async def process_growth(message: types.Message, state: FSMContext):
    try:
        growth = int(message.text)
        if growth < 50 or growth > 250:  # Допустимый диапазон роста
            await message.reply("Некорректный рост. Пожалуйста, введите число от 50 до 250.")
            return
        await state.update_data(growth=growth)
        await message.reply("Введите свой вес в килограммах (число):")
        await UserState.next()
    except ValueError:
        await message.reply("Некорректный ввод. Пожалуйста, введите число.")


@dp.message_handler(state=UserState.weight)
async def process_weight(message: types.Message, state: FSMContext):
    try:
        weight = float(message.text)
        if weight <= 0 or weight > 500: # Допустимый диапазон веса
            await message.reply("Некорректный вес. Пожалуйста, введите число больше 0 и меньше 500.")
            return
        await state.update_data(weight=weight)
        data = await state.get_data()
        age = data['age']
        growth = data['growth']
        weight = data['weight']

        # Расчет калорий по формуле Миффлина-Сан Жеора (для женщин)

        calories = int((10 * weight) + (6.25 * growth) - (5 * age) - 161)
        await message.reply(f"Ваша примерная суточная норма калорий: {max(calories, 0)} ккал (женщины).  Для мужчин значение будет другим.")

        await state.finish()
    except ValueError:
        await message.reply("Некорректный ввод. Пожалуйста, введите число.")


# Inline клавиатура задание 14.3 к нопке "Купить"
@dp.message_handler(text='Купить', state='*')  # Обработчик для кнопки "Купить"
async def get_buying_list(message: types.Message):
    products = [
        {"name": "Product 1", "description": "Описание 1", "price": 100, "photo": "mg.jpg"},
        {"name": "Product 2", "description": "Описание 2", "price": 200, "photo": "ca.jpg"},
        {"name": "Product 3", "description": "Описание 3", "price": 300, "photo": "chai.png"},
        {"name": "Product 4", "description": "Описание 4", "price": 400, "photo": "bcomp.jpg"},
    ]

async def main():
    await dp.start_polling()

    if __name__ == '__main__':
       asyncio.run(main())
