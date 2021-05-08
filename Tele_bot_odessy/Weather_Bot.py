import telebot
import pyowm
from pyowm.utils.config import get_default_config

bot = telebot.TeleBot("1830822619:AAHECzZp_mNiB6AWmdcLUDbBu4BsJOOEHr8")
owm = pyowm.OWM('2b8f81b5b81eca36cd0e836a3dcfcde1')
mgr = owm.weather_manager()
config_dict = get_default_config()
config_dict['language'] = 'ru'


@bot.message_handler(commands=['start', 'help'])
def start(message):
    bot.send_message(message.chat.id, "Привет, что бы узнать погоду - просто напиши название города.")


@bot.message_handler(content_types=['text'])
def send_weather(message):
    observation = mgr.weather_at_place(message.text)
    w = observation.weather
    temp = w.temperature('celsius')['temp']

    answer = "В городе " + message.text + " сейчас - " + w.detailed_status + "\n"
    answer += "Температура - " + str(temp) + " градусов" + "\n"

    if temp < 10:
        answer = answer + "На улице холодно, оденьтесь тепло."
    elif temp < 20:
        answer = answer + "На улице прохладно, возьмите что-то теплое."
    else:
        answer = answer + "На улице тепло, одевайте что угодно =)"

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True)
