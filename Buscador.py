import telebot

TOKEN = '234640505:AAH-CkZTORE4ItAurfEhvIZMLwBissgYsc8' #Ponemos nuestro TOKEN generado con el @BotFather  
bot = telebot.TeleBot(TOKEN)                         #Creamos nuestra instancia "mi_bot" a partir de ese TOKEN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola, queres buscar un video?")

@bot.message_handler(commands=['buscar_video'])
def send_welcome(message):
    bot.reply_to("Hola, que video queres buscar")

bot.polling()
