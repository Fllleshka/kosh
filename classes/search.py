from classes.imports import *

class searchprofiles:

    # Инициализация переменных класса
    def __init__(self, bot, message):
        self.bot = bot
        self.message = message
        self.database = DataBase(pathtodatabase)

    # Импорт всех данных
    def importdatesfromdatabase(self, argument):
        match (argument):
            case "Тренер":
                # Запрос на вывод всех тренеров
                request_coach = "SELECT last_name, first_name, id_telegram, rating FROM users WHERE id_type = 1"
                dates = self.database.selectfromdatabase(request_coach)
            case "Спортсмен":
                # Запрос на вывод всех спорсменон
                request_sportsmen = "SELECT last_name, first_name, id_telegram, rating FROM users WHERE id_type = 2"
                dates = self.database.selectfromdatabase(request_sportsmen)
        return dates

    # Печать данных
    def printdates(self, argument):

        datesfromdatabase = self.importdatesfromdatabase(argument)

        # Создание меню
        markup = telebot.types.InlineKeyboardMarkup()

        # Кнопки навигации
        leftbutton = telebot.types.InlineKeyboardButton("<", callback_data='left')
        rightbutton = telebot.types.InlineKeyboardButton(">", callback_data='right')
        centerbutton = telebot.types.InlineKeyboardButton("0/0", callback_data='None')
        markup.add(leftbutton, centerbutton, rightbutton)

        # Кнопка связаться
        url = "t.me/user?id=" + str(datesfromdatabase[0][2])
        name = str(datesfromdatabase[0][0]) + " " + str(datesfromdatabase[0][1])
        user = telebot.types.InlineKeyboardButton(name, url = url)
        markup.add(user)

        #self.importdatesfromdatabase()

        self.bot.send_message(self.message.chat.id, "111", reply_markup=markup)