from classes.imports import *

class searchprofiles:

    # Инициализация переменных класса
    def __init__(self, bot, message, role):
        self.bot = bot
        self.message = message
        self.database = DataBase(pathtodatabase)
        self.datesfromdatabase = self.importdatesfromdatabase(role)

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
    def bottombuttons(self, markup, index, countmenues, url):

        # Кнопка связаться
        if url == "tg://user?id=None":
            tgforsendphoto = telebot.types.InlineKeyboardButton("Связаться", callback_data = "wrong_url")
        else:
            tgforsendphoto = telebot.types.InlineKeyboardButton("Связаться", url=url)
        markup.add(tgforsendphoto)
        # Левая стрелка
        leftcallbackdata = 'print.left|' + str(index)
        leftbutton = telebot.types.InlineKeyboardButton("<", callback_data=leftcallbackdata)
        # Правая стрелка
        rightcallbackdata = 'print.right|' + str(index)
        rightbutton = telebot.types.InlineKeyboardButton(">", callback_data=rightcallbackdata)
        # Центральный сектор с сётчиком
        textcenterbutton = str(index) + " / " + str(countmenues)
        if index < 0:
            textcenterbutton = "0 / " + str(countmenues)
        if index > countmenues:
            textcenterbutton = str(index) + " / " + str(countmenues)
        centerbutton = telebot.types.InlineKeyboardButton(textcenterbutton, callback_data='print.None')
        markup.add(leftbutton, centerbutton, rightbutton)

        return markup

    # Формирование профиля
    def createprofiledates(self, dates, index, images):
        returntext = []
        imageuser = images.startpathprofile + str(dates[index][0]) + "/profile.png"
        returntext.append(imageuser)
        url = "tg://user?id=" + str(dates[index][0])
        returntext.append(url)
        name = str(dates[index][1]) + " " + str(dates[index][2]) + "\n" + "R: " + str(dates[index][3])
        returntext.append(name)
        return returntext

    # Печать данных
    def printdates(self, argument, bot, images):

        # Получаем все записи по нашему запросу
        self.datesfromdatabase = self.importdatesfromdatabase(argument)

        print(f"======{argument}======")
        for element in self.datesfromdatabase:
            print(element)
        print(f"======{argument}======")
        # Проверка данные на наличие, если нет, то выводим сообщение
        if len(self.datesfromdatabase) != 0:

            # Определяем количество строк нужных нам в нашем списке
            countmenues = len(self.datesfromdatabase) - 1
            print("Количество строк в массиве: ", countmenues)

            datesforsendphoto = self.createprofiledates(self.datesfromdatabase, 0, images)
            markupsendphoto = telebot.types.InlineKeyboardMarkup()

            # Кнопки навигации
            markupsendphoto = self.bottombuttons(markupsendphoto, 0, countmenues, datesforsendphoto[1])

            self.bot.send_photo(self.message.chat.id,
                                photo=open(datesforsendphoto[0], 'rb'),
                                caption=datesforsendphoto[2],
                                reply_markup = markupsendphoto)

        else:
            self.bot.send_message(self.message.chat.id, "К сожалению нету анкет подходящих вам.\nПопробуйте позже...")

        @bot.callback_query_handler(func=lambda call: True)
        def callbackdata(call):
            # Получаем все записи по нашему запросу
            datesfromdatabase = self.importdatesfromdatabase(argument)
            print("Работа функции обработки кнопок")
            markupsendphoto = telebot.types.InlineKeyboardMarkup()
            commands = call.data.split("|")

            match (commands[0]):
                case "print.left":
                    if self.checkleftbarruer(commands[1]) == True:
                        self.bot.answer_callback_query(callback_query_id=call.id,
                                                       text="Дальше нету анкет(\nЛистайте вправо...")
                    else:
                        if int(commands[1]) <= 0:
                            indexforbottombuttons = 0
                        else:
                            indexforbottombuttons = int(commands[1]) - 1
                        # Получаем все записи по нашему запросу
                        #datesfromdatabase = self.importdatesfromdatabase(argument)
                        # Подготавливаем данные для изменения
                        newdatesforperson = self.createprofiledates(datesfromdatabase, indexforbottombuttons, images)
                        print(newdatesforperson)
                        newtext = newdatesforperson[2]
                        newphoto = open(newdatesforperson[0], 'rb')
                        newurl = newdatesforperson[1]
                        newmarkup = self.bottombuttons(markupsendphoto, indexforbottombuttons, countmenues, newurl)

                        # Изменение данных сообщения
                        self.bot.edit_message_media(chat_id=call.message.chat.id,
                                                    message_id=call.message.message_id,
                                                    media=telebot.types.InputMedia(
                                                        type='photo',
                                                        media=newphoto,
                                                        caption=newtext),
                                                    reply_markup=newmarkup)
                case "print.right":
                    print(argument)
                    # Получаем все записи по нашему запросу
                    #datesfromdatabase = self.importdatesfromdatabase(argument)

                    if self.checkrightbarruer(commands[1], self.datesfromdatabase) == True:
                        self.bot.answer_callback_query(callback_query_id=call.id,
                                                       text="Дальше нету анкет(\nЛистайте влево...")
                    else:
                        if int(commands[1]) >= len(datesfromdatabase):
                            indexforbottombuttons = len(datesfromdatabase)
                        else:
                            indexforbottombuttons = int(commands[1]) + 1

                        # Подготавливаем данные для изменения
                        newdatesforperson = self.createprofiledates(datesfromdatabase, indexforbottombuttons, images)
                        print(newdatesforperson)
                        newtext = newdatesforperson[2]
                        newphoto = open(newdatesforperson[0], 'rb')
                        newurl = newdatesforperson[1]
                        newmarkup = self.bottombuttons(markupsendphoto, indexforbottombuttons, countmenues, newurl)

                        # Изменение данных сообщения
                        self.bot.edit_message_media(chat_id=call.message.chat.id,
                                               message_id=call.message.message_id,
                                               media=telebot.types.InputMedia(
                                                   type='photo',
                                                   media=newphoto,
                                                   caption=newtext),
                                               reply_markup=newmarkup)
                case "wrong_url":
                    self.bot.answer_callback_query(callback_query_id=call.id, text="Хм...\n\nНаписать не получится(\nCсылка на профиль битая(")

    # Проверка нажатия кнопки влево при самой первой анкете
    def checkleftbarruer(self, index):
        print("Достингут левый барьер ", index, "\t", type(index))
        if int(index) == 0:
            return True
        else:
            return False

    # Проверка нажатия кнопки право при самой последней анкете
    def checkrightbarruer(self, index, dates):
        print("Достингут правый барьер ", index, "\t", type(index), "\t", len(dates) - 1)
        if int(index) == len(dates) - 1:
            return True
        else:
            return False