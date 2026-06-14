import telebot
from telebot import types
bot = telebot.TeleBot('8685421260:AAGRS3FfkLvB9CZZbxbtOpvV-dAKXhtd6TE')


@bot.message_handler(commands=['start'])
def start(message):
   keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
   game_dev = types.KeyboardButton('Game developer')
   ai_dev = types.KeyboardButton('Ai development on python')
   software_dev = types.KeyboardButton('Software development')
   web_dev = types.KeyboardButton('Web development')
   data_dev = types.KeyboardButton('DataScience development')
   keyboard.add(game_dev,ai_dev,software_dev,web_dev,data_dev)
   send_message = f"<b>Hello my dear</b>\n which type of quiz you want to solve?"
   bot.send_message(message.chat.id,send_message,parse_mode='html',reply_markup=keyboard)
@bot.message_handler(content_types=['text'])
def mess(message):
   if message.text =='Game developer':
       markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
       btn1 = types.KeyboardButton('For mobile devices')
       btn2 = types.KeyboardButton('PlayStation')
       btn3 = types.KeyboardButton('Laptops/PC')
       btn4 = types.KeyboardButton('Web-games')
       btn5 = types.KeyboardButton('Start test again')
       markup.add(btn1,btn2,btn3,btn3,btn4,btn5)
       final_message = f"<b>Cool!!</b>\n The game development is best choise\n which platform for you want to develop? "
       bot.send_message(message.chat.id,final_message,parse_mode='html',reply_markup=markup)
   elif message.text == 'For mobile devices':
       markup = types.InlineKeyboardMarkup()
       unity = types.InlineKeyboardButton("Look course on Unity",url="https://learn.unity.com/")
       markup.add(unity)
       final_message=f"For mobile app development we actualy use the Unity platform"
       bot.send_message(message.chat.id,final_message,parse_mode='html',reply_markup=markup)
   elif message.text == 'Start test again':
       send_mess = 'You wanna to start  from scrath again?/Choose another program'
       keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True,row_width=2)
       game_dev = types.KeyboardButton('Game developer')
       ai_dev = types.KeyboardButton('Ai development on python')
       software_dev = types.KeyboardButton('Software development')
       web_dev = types.KeyboardButton('Web development')
       data_dev = types.KeyboardButton('DataScience development')
       keyboard.add(game_dev,ai_dev,software_dev,web_dev,data_dev)
       bot.send_message(message.chat.id,send_message,parse_mode='html',reply_markup=keyboard)
    
#python main.py

bot.infinity_polling()
