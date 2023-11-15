import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['help'])
def tests(message): 
    bot.reply_to(message,
    """
    Чем я могу помочь?
    """)
    

@bot.message_handler(commands=["start"])
def tests(message): 
    bot.send_message(message.from_user.id, 'Привет')


bot.infinity_polling()