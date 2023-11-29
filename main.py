import telebot
from telebot import types

bot = telebot.TeleBot('6389786107:AAE_6Zit00pJ1tVupUbsd55u7SUmSpXMD8A')


@bot.message_handler(commands=['start'])
def first(message):
    markup = types.ReplyKeyboardMarkup()
    bot1 = types.KeyboardButton('Я грущу')
    bot2 = types.KeyboardButton('*Я ОЧЕНЬ УСТАЛ*')
    markup.row(bot1, bot2)
    bot.send_message(message.chat.id, ' [Приветсвую тебя](https://imagename.ru/imgbig/imagename_ru_19702.jpg )',
                     parse_mode='Markdown')
    bot.register_next_step_handler(message, txt)


def txt(message):
    if message.text == 'Я грущу':
        bot.send_message(message.chat.id,
                         ' [Не грусти, лови котеек](https://masterpiecer-images.s3.yandex.net/0e7616ce7c6e11eead5e3abd0be4d755:upscaled)',
                         parse_mode='Markdown')
    elif message.text == '*Я ОЧЕНЬ УСТАЛ*':
        bot.send_message(message.chat.id,
                         '[Просто нажми на кнопку](https://www.myinstants.com/ru/instant/motivatsiiu-nado-podniat-7858/)',
                         parse_mode='Markdown')


# ЕСЛИ КНОПКИ НЕ СРАБОТАЮТ РАЗКОВЫЧТИ ТО ЧТО СНИЗУ, А ВЕРХ УБЕРИТЕ ПОЖАЛУЙСТА
'''@bot.message_handler(commands=['start'])
def main(message):
	bot.send_message(message.chat.id, '*Приветсвую тебя*', parse_mode='Markdown')

@bot.message_handler(commands=['tired'])
def main(message):
	bot.send_message(message.chat.id, ' [Не грусти, лови котеек](https://masterpiecer-images.s3.yandex.net/0e7616ce7c6e11eead5e3abd0be4d755:upscaled)', parse_mode='Markdown')

@bot.message_handler(commands=['vtired'])
def main(message):
	bot.send_message(message.chat.id, '[Просто нажми на кнопку](https://www.myinstants.com/ru/instant/motivatsiiu-nado-podniat-7858/)', parse_mode='Markdown')'''

bot.infinity_polling()