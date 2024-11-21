from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, Bot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, CallbackContext

# Функция для создания главной клавиатуры
def start_keyboard():
    keyboard = [['Купить']]
    return ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

# Функция, вызываемая при старте бота
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Добро пожаловать в магазин!', reply_markup=start_keyboard())

# Функция для получения списка продуктов
def get_buying_list(update: Update, context: CallbackContext) -> None:
    message_text = ""
    products = [
        {"name": "Product1", "description": "описание 1", "price": 100},
        {"name": "Product2", "description": "описание 2", "price": 200},
        {"name": "Product3", "description": "описание 3", "price": 300},
        {"name": "Product4", "description": "описание 4", "price": 400}
    ]

    for product in products:
        message_text += f'Название: {product["name"]} | Описание: {product["description"]} | Цена: {product["price"]}\n'

    context.bot.send_photo(chat_id=update.message.chat_id, photo='URL_или_путь_к_изображению')

    message_text += "Выберите продукт для покупки:"
    
    # Создаем Inline клавиатуру
    inline_keyboard = [
        [InlineKeyboardButton("Product1", callback_data="product_buying")],
        [InlineKeyboardButton("Product2", callback_data="product_buying")],
        [InlineKeyboardButton("Product3", callback_data="product_buying")],
        [InlineKeyboardButton("Product4", callback_data="product_buying")]
    ]
    reply_markup = InlineKeyboardMarkup(inline_keyboard)

    update.message.reply_text(message_text, reply_markup=reply_markup)

# Хэндлер для текстового сообщения "Купить"
def message_handler(update: Update, context: CallbackContext) -> None:
    if update.message.text == "Купить":
        get_buying_list(update, context)

# Функция для подтверждения покупки
def send_confirm_message(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    query.edit_message_text(text="Вы успешно приобрели продукт!")

# Основная функция для запуска бота
def main():
    updater = Updater("BOT_TOKEN")

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, message_handler))
    dp.add_handler(CallbackQueryHandler(send_confirm_message, pattern="product_buying"))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()


### Описание кода:
1. Главная клавиатура: Создается с одной кнопкой "Купить".
2. get_buying_list: Формирует текст с информацией о продуктах и отправляет Inline клавиатуру с кнопками для выбора продуктов.
3. message_handler: Обрабатывает текстовое сообщение и вызывает get_buying_list, если текст равен "Купить".
4. send_confirm_message: Обрабатывает нажатие на кнопки продуктов, отправляет сообщение о покупке.
5. Доступны слоты для отправки изображений к продуктам.
###Дополнение к боту из задания 13_6
