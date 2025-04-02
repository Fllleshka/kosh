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
                request_coach = 'SELECT users.id_telegram, users.first_name, users.last_name, users.rating, town.name as "Город", kind_sport.name as "Тип спорта", level_training.name as "Уровень подготовки", place.name as "Место проведения" FROM users, kind_sport, town, level_training, place WHERE   id_type = 1 AND users.id_kind = kind_sport.id_kind AND users.id_town = town.id_town AND users.id_level = level_training.id_level AND users.id_place = place.id_place'
                dates = self.database.selectfromdatabase(request_coach)
            case "Спортсмен":
                # Запрос на вывод всех спорсменон
                request_sportsmen = 'SELECT users.id_telegram, users.first_name, users.last_name, users.rating, town.name as "Город", kind_sport.name as "Тип спорта", level_training.name as "Уровень подготовки", place.name as "Место проведения" FROM users, kind_sport, town, level_training, place WHERE   id_type = 2 AND users.id_kind = kind_sport.id_kind AND users.id_town = town.id_town AND users.id_level = level_training.id_level AND users.id_place = place.id_place'
                dates = self.database.selectfromdatabase(request_sportsmen)
        return dates

    # Выбираем данные для меню
    def selectdatesformenu(self, startindex, endindex, dates, images, markup):
        while startindex < endindex:
            imageuser = images.startpathprofile + str(dates[startindex][0]) + "/profile.png"
            url = "tg://user?id=" + str(dates[startindex][0])
            name = str(dates[startindex][1]) + " " + str(dates[startindex][2])
            user = telebot.types.InlineKeyboardButton(name, url=url)
            markup.add(user)
            startindex += 1

        return markup

    # Создание кнопок внизу списка
    def bottombuttons(self, markup, countmenues):
        leftbutton = telebot.types.InlineKeyboardButton("<", callback_data='print.left')
        rightbutton = telebot.types.InlineKeyboardButton(">", callback_data='print.right')
        textcenterbutton = "1/" + str(countmenues)
        centerbutton = telebot.types.InlineKeyboardButton(textcenterbutton, callback_data='print.None')
        markup.add(leftbutton, centerbutton, rightbutton)
        return markup

    # Печать данных
    def printdates(self, argument, bot, images):

        # Получаем все записи по нашему запросу
        datesfromdatabase = self.importdatesfromdatabase(argument)
        # Создание меню
        markup = telebot.types.InlineKeyboardMarkup()

        # Проверка данные на наличие, если нет, то выводим сообщение
        if len(datesfromdatabase) != 0:

            # Определяем количество менюшек в нашем списке
            countmenues = len(datesfromdatabase)
            print("Количество менюшек по 5 позиций:", countmenues)

            markup = self.selectdatesformenu(0, 5, datesfromdatabase, images, markup)
            print("========================")
            for elem in range(0, countmenues):
                print(elem * 5, "\t", (elem+1)*5)
            print("========================")

            '''for element in datesfromdatabase:
                indexelem = datesfromdatabase.index(element)
                imageuser = images.startpathprofile + str(datesfromdatabase[indexelem][0]) + "/profile.png"
                url = "tg://user?id=" + str(datesfromdatabase[indexelem][0])
                name = str(datesfromdatabase[indexelem][1]) + " " + str(datesfromdatabase[indexelem][1])
                user = telebot.types.InlineKeyboardButton(name, url = url)
                print(element, "\t", imageuser)
                markup.add(user)'''

            # Кнопки навигации
            self.bottombuttons(markup, countmenues)

            markup2 = telebot.types.InlineKeyboardMarkup()
            centerbutton = telebot.types.InlineKeyboardButton("Тестовая кнопка", callback_data='print.None')
            markup2.add(centerbutton)

            self.bot.send_message(self.message.chat.id, "Список тренеров", reply_markup=markup)
        else:
            self.bot.send_message(self.message.chat.id, "К сожалению нету анкет подходящих вам.\nПопробуйте позже...")

        @bot.callback_query_handler(func=lambda call: True)
        def callbackdata(call):
            match (call.data):
                case "print.left":
                    bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                        message_id=call.message.message_id,
                                                        reply_markup=markup2)
                case "print.right":
                    bot.edit_message_reply_markup(chat_id=call.message.chat.id,
                                                        message_id=call.message.message_id,
                                                        reply_markup=markup2)