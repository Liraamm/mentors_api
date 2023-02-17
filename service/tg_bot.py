
import telebot


bot = telebot.TeleBot('6145098124:AAFQoPskvUdrAGL5hbECIdFcFtxQNI1aE5c')


@bot.message_handler(commands=['start'])
def start(message):
    mess = f'Привет, {message.from_user.first_name}, ваша заявка подтверждена'
    bot.send_message(message.chat.id, mess)
    





bot.polling(none_stop=True)