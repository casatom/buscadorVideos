from pyTelegramBotAPI import telebot 

TOKEN = '244028879:AAF8abnnbX_wwrjZpQMqCXqL8wOK6QrT44w' 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def command_help(message):
    bot.reply_to(message, "Hola, escribe /buscar_cancion y el nombre de la cancion y te enviaremos un  link")


bot.polling()



