import telebot 

TOKEN = '244028879:AAF8abnnbX_wwrjZpQMqCXqL8wOK6QrT44w' 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola, soy tu parlante SAIKO, que puedo hacer por vos?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.polling()