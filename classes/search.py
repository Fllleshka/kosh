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


        # Создание меню
        markup = telebot.types.InlineKeyboardMarkup()


        leftbutton = telebot.types.InlineKeyboardButton("<", callback_data='left')
        rightbutton = telebot.types.InlineKeyboardButton(">", callback_data='right')
        centerbutton = telebot.types.InlineKeyboardButton("0/0", callback_data='None')
        markup.add(leftbutton, centerbutton, rightbutton)


        #self.importdatesfromdatabase()

        self.bot.send_message(self.message.chat.id, "111", reply_markup=markup)