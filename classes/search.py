from classes.imports import *

class searchprofiles:

    # Инициализация переменных класса
    def __init__(self, bot, message):
        self.bot = bot
        self.message = message
        self.database = DataBase(pathtodatabase)

    # Импорт всех данных
    def importdatesfromdatabase(self):
        # Запрос на вывод всех тренеров
        request_coach = "SELECT last_name, first_name, id_telegram FROM users WHERE id_type = 1"
        # Запрос на вывод всех спорсменон
        request_coach = "SELECT last_name, first_name, id_telegram FROM users WHERE id_type = 1"

        dates = self.database.selectfromdatabase(request)
        print(dates)

    # Печать данных
    def printdates(self):

        url = "tg://user?id=1871580124"
        messagetext="Владислав"

        btn = telebot.types.InlineKeyboardButton(messagetext, url)

        # Создание меню
        markup = telebot.types.InlineKeyboardMarkup()
        markup.add(btn)

        self.importdatesfromdatabase()

        self.bot.send_message(self.message.chat.id, "111", reply_markup=markup)