# Файл работы с базой данных
from classes.database import *
# Константные данные для работы
from classes.dates import *
# Кнопочки для создания притки
from classes.buttons import *
# Файл для работы с профилем
from classes.profile import *

# Инициализация бота
bot = telebot.TeleBot(tokenbot)
# Инициализация кнопок
buttonsmarkup = buttons()
# Инициализация сообщений
messagestouser = messages()
# Инициализация картинок
imagestouser = images()
# Инициалзиация класса отвечающего за профиль
profileinf = profile(bot, messagestouser, buttonsmarkup)