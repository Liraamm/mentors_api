import telebot


bot = telebot.TeleBot()


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)





bot.polling(none_stop=True)
