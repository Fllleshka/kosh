# Файл работы с базой данных
from classes.database import *
# Константные данные для работы
from classes.dates import *
# Кнопочки для создания притки
from classes.buttons import *

# Инициализация бота
bot = telebot.TeleBot(tokenbot)
# Инициализация кнопок
buttonsmarkup = buttons()
# Инициализация сообщений
messagestouser = messages()
# Инициализация картинок
imagestouser = images()