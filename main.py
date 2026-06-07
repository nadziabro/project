import telebot
from telebot import types
bot = telebot.TeleBot('8685421260:AAGRS3FfkLvB9CZZbxbtOpvV-dAKXhtd6TE')

@bot.message_handler(commands=['start'])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    games = types.KeyboardButton('Создание игр')
    mobile_app = types.KeybboadButton('Мобильная разроботка')
    computer_app = types.KeyboardButton('ИРазроботчик софта')
    data = types.KeyboardButton('Дата аналитика')
    web_app = types.KeyboardButton('Веб разроботка')
    artificial_intellegence = types.KeyboardButton('Разроботка искуственного интелекта')
    keyboard.add(games,mobile_app,computer_app,data,web_app,artificial_intellegence)

    send_msg = f"<b>Привет!</b> \n Какой именно курс или направление тебя интересует?"
    bot.send_message(message.chat.id, send_msg, parse_mode="html",reply_markup=keyboard)
bot.polling(none_stop=True)


@bot.message_handler(content_types==['text'])
def  game_msg(message):
    if message.text=='Создвние игр':
        murcup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
        btn1=types.KeyboardButton('Под мобильные телефоны')
        btn2=types.KeyboardButton('Комьютеры и консоли')
        btn3=types.KeyboardButton('Виртуальная реальность')
        btn4=types.KeyboardButton('Браузерская игра')
        btn5=types.KeyboardButton('Вернуться в начальное меню')
