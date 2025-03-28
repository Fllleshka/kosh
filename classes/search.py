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

    # Печать данных
    def printdates(self, argument, bot, images):

        # Получаем все записи по нашему запросу
        datesfromdatabase = self.importdatesfromdatabase(argument)

        # Создание меню
        markup = telebot.types.InlineKeyboardMarkup()

        # Кнопка связаться
        if len(datesfromdatabase) != 0:
            for element in datesfromdatabase:
                indexelem = datesfromdatabase.index(element)
                imageuser = images.startpathprofile + str(datesfromdatabase[indexelem][0]) + "/profile.png"
                url = "tg://user?id=" + str(datesfromdatabase[indexelem][0])
                name = str(datesfromdatabase[indexelem][1]) + " " + str(datesfromdatabase[indexelem][1])
                user = telebot.types.InlineKeyboardButton(name, url = url)
                print(element, "\t", imageuser)
                markup.add(user)

            # Кнопки навигации
            leftbutton = telebot.types.InlineKeyboardButton("<", callback_data='print.left')
            rightbutton = telebot.types.InlineKeyboardButton(">", callback_data='print.right')
            centerbutton = telebot.types.InlineKeyboardButton("0/0", callback_data='print.None')
            markup.add(leftbutton, centerbutton, rightbutton)



            changemessage = self.bot.send_message(self.message.chat.id, "Список тренеров", reply_markup=markup).message_id
        else:
            changemessage = self.bot.send_message(self.message.chat.id, "К сожалению нету анкет подходящих вам.\nПопробуйте позже...")

        @bot.callback_query_handler(func=lambda call:call.data.startswith('print.'))
        def callbackdata(call):
            match (call.data):
                case "print.left":
                    editmessage = bot.edit_message_text(chat_id=call.message.chat.id,
                                                        message_id=changemessage,
                                          text="Нажми1")
                case "print.right":
                    editmessage = bot.edit_message_text(chat_id=call.message.chat.id,
                                          message_id=changemessage,
                                          text="Нажми2")