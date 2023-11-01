import config
import telebot

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=["start"])
def tests(message): 
    bot.send_message(message.from_user.id, 'Привет')

@bot.message_handler(content_types=["text"])
def tests(message): 
    bot.send_message(message.chat.id, message.text)


bot.polling(none_stop=True)
