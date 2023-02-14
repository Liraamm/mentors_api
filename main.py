import telebot


bot = telebot.TeleBot('6011930948:AAEV7fmaBR4zI2jX3Y-OjTbSU8MnFy3v6_I')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name}'
    bot.send_message(message.chat.id, mess)





bot.polling(none_stop=True)
