import telebot
from telebot import types
bot = telebot.TeleBot('8878639660:AAFxY-1XWBvddKqwpOETDmbjJfcHjAQdsK4')

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
    btn1 = types.KeyboardButton('My favorite')
    btn2 = types.KeyboardButton('Popular')
    btn3 = types.KeyboardButton('Genre')
    btn4 = types.KeyboardButton('Search')
    markup.add(btn1, btn2, btn3, btn4)
    send_massage = f"<b>Hello niger! </b> whasap with it vanilla face?\nWhich janre of music do you like?"
    bot.send_message(message.chat.id,send_massage,parse_mode='html',reply_markup=markup)
bot.infinity_polling()
