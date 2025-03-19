from classes.imports import *

class searchprofiles:

    # Инициализация переменных класса
    def __init__(self, bot, message):
        self.bot = bot
        self.message = message

    # Импорт всех данных

    # Печать данных
    def printdates(self):

        url = "tg://user?id=1871580124"
        messagetext="Владислав"

        btn = telebot.types.InlineKeyboardButton(messagetext, url)

        # Создание меню
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(btn)

        self.bot.send_message(self.message.chat.id, "111", reply_markup=markup)
