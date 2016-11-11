import telebot
import urllib.request
import urllib.parse
import re

TOKEN = '234640505:AAH-CkZTORE4ItAurfEhvIZMLwBissgYsc8' #Ponemos nuestro TOKEN generado con el @BotFather  
bot = telebot.TeleBot(TOKEN)                         #Creamos nuestra instancia "mi_bot" a partir de ese TOKEN

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Hola, queres buscar un video?")

@bot.message_handler(func=lambda message: True)
def buscar_video(message):
	print("entre")
	query_string = urllib.parse.urlencode({"search_query" : message.text})
	html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
	print("http://www.youtube.com/watch?v=" + search_results[0])	
	bot.reply_to(message, "http://www.youtube.com/watch?v=" + search_results[0])

bot.polling()
