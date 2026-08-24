from transliterate import to_cyrillic, to_latin

import telebot

TOKEN = '8939738083:AAHNNN9LCJ53VKS9V1fD13sst5cQgvj_QOI'
bot = telebot.TeleBot(TOKEN, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    
	bot.reply_to(message, "Assalomu Alaykum, Xush kelibsiz!\nMatn kiriting/Матн киритинг:\n")

@bot.message_handler(func=lambda message: True)
def echo_message(message):
    msg = message.text

    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)   
    bot.reply_to(message, javob)

bot.polling()






matin = input("Matn kiriting/Матн киритинг:\n")

if matin.isascii():
    print(to_cyrillic(matin))
else:
    print(to_latin(matin))    