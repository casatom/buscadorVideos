import telebot 

TOKEN = '280355257:AAGs6hryt9rs_ZBIHNJxzp1qIowZLhe486s' 

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def command_help(message):
    bot.reply_to(message, "Hola, escribe /buscar_cancion y el nombre de la cancion y te enviaremos un  link")

bot.polling()



