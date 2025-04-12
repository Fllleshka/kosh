import os.path
from datetime import *

from telebot.types import PreparedInlineMessage
from urllib3 import request

from classes.imports import *

# Импорт библиотеки для работы с ботом
import telebot
import json

class profile:
    # Инициализация переменных
    def __init__(self, bot, messagestouser, buttonsmarkup, imagestouser, tids):
        self.bot = bot
        self.pathdatabase = pathtodatabase
        self.messagestouser = messagestouser
        self.buttonsmarkup = buttonsmarkup
        self.imagestouser = imagestouser
        self.tids = tids
        self.fulldates = []

        self.first_name_date = ""
        self.last_name_date = ""
        self.middle_name_date = ""
        self.birth_date_date = ""
        self.raiting = 0
        self.telegramid = None
        self.town_date = ""
        self.town_date_name = ""
        self.typesport_date = ""
        self.typesport_date_name = ""
        self.level_date = ""
        self.level_date_name = ""
        self.place_date = ""
        self.place_date_name = ""
        self.accaunt_type = ""
        self.accaunt_type_name = ""
        self.description_date = ""

    # Проверка на существование профиля в базе данных
    def existencecheck(self, message):
        flag = False
        # Определяем telegramId
        self.telegramid = message.chat.id
        # Запрос со всеми telegramid которые есть в базе
        base = DataBase(pathtodatabase)
        request = "SELECT id_telegram FROM users"
        # Полученные из базы данные
        dates = base.selectfromdatabase(request)
        # Формируем список всех типов мест
        ids = []
        for elem in dates:
            if elem[0] == self.telegramid:
                flag = True
        return flag

    # Вывод всех данных
    def printdates(self):
        print("==================")
        print(f"Имя: \t\t\t\t\t{self.first_name_date}")
        print(f"Фамилия: \t\t\t\t{self.last_name_date}")
        print(f"Отчество: \t\t\t\t{self.middle_name_date}")
        print(f"Возраст: \t\t\t\t{self.calc_age(self.birth_date_date)}\t{self.birth_date_date}")
        print(f"Рейтинг: \t\t\t\t{self.raiting}")
        print(f"TelegramID: \t\t\t{self.telegramid}")
        print(f"Город: \t\t\t\t\t{self.town_date}\t{self.town_date_name}")
        print(f"Вид спорта: \t\t\t{self.typesport_date}\t{self.typesport_date_name}")
        print(f"Уровень подготовки: \t{self.level_date}\t{self.level_date_name}")
        print(f"Место проведения: \t\t{self.place_date}\t{self.place_date_name}")
        print(f"Тип аккаунта: \t\t\t{self.accaunt_type}\t{self.accaunt_type_name}")
        print(f"Описание: \t\t\t\t{self.description_date}")
        print("==================")

    # Функция вычисления возраста
    def calc_age(self, birthdate):
        # Преобразуем данные из строки в массив
        splitbirthdate = birthdate.split(".")
        intbirthdate = []
        # Преобразуем в чело численный тип и выставляем правильный порядок
        for elem in reversed(splitbirthdate):
            intbirthdate.append(int(elem))
        today = datetime.now().date()
        birthdatedate = date(intbirthdate[0], intbirthdate[1], intbirthdate[2])
        age = today.year - birthdatedate.year - ((today.month, today.day) < (birthdatedate.month, birthdatedate.day))
        return age

    # Функция вычисления id в зависимой таблице
    def seart_id_in_database(self, dates, table):
        id = 0
        match(table):
            case "town":
                # Запрос к базе данных по id выбранного города
                base = DataBase(pathtodatabase)
                req = "SELECT id_town FROM town WHERE name='" + dates + "'"
                # Полученные из базы данные
                id = base.selectfromdatabase(req)[0][0]

            case "type_sport":
                # Запрос к базе данных по id выбранного типа спорта
                base = DataBase(pathtodatabase)
                req = "SELECT id_kind FROM kind_sport WHERE name='" + dates + "'"
                # Полученные из базы данные
                id = base.selectfromdatabase(req)[0][0]

            case "level_training":
                # Запрос к базе данных по id выбранного уровня подготовки
                base = DataBase(pathtodatabase)
                req = "SELECT id_level FROM level_training WHERE name='" + dates + "'"
                # Полученные из базы данные
                id = base.selectfromdatabase(req)[0][0]

            case "place":
                # Запрос к базе данных по id выбранного места тренировки
                base = DataBase(pathtodatabase)
                req = "SELECT id_place FROM place WHERE name='" + dates + "'"
                # Полученные из базы данные
                id = base.selectfromdatabase(req)[0][0]

            case "accaunt_type":
                # Запрос к базе данных по id выбранного типа аккаунта
                base = DataBase(pathtodatabase)
                req = "SELECT id_type FROM accaunt_type WHERE name='" + dates + "'"
                # Полученные из базы данные
                id = base.selectfromdatabase(req)[0][0]

            case _:
                print("Ошибка обработки запроса")
        return id

    # Добавление имя для тренера, а так же определяем telegramid
    def first_name(self, message):
        # Определяем telegramId
        self.telegramid = message.chat.id
        # Отправляем сообщение
        self.bot.reply_to(message, self.messagestouser.messagecoachfirstname,
                            reply_markup=self.buttonsmarkup.retunmarkup("Null"))
        self.bot.register_next_step_handler(message, self.last_name)

    # Добавление фамилия для тренера, а так же выставляем рейтинг 0
    def last_name(self, message):
        self.first_name_date = message.text
        # Отправляем сообщение
        self.bot.reply_to(message, self.messagestouser.messagecoachlastname,
                            reply_markup=self.buttonsmarkup.retunmarkup("Null"))
        self.bot.register_next_step_handler(message, self.middle_name)

    # Добавление отчество для тренера
    def middle_name(self, message):
        self.last_name_date = message.text
        # Отправляем сообщение
        self.bot.reply_to(message, self.messagestouser.messagecoachmiddlename,
                            reply_markup=self.buttonsmarkup.retunmarkup("Null"))
        self.bot.register_next_step_handler(message, self.birth_date)

    # Добавление даты рождения
    def birth_date(self, message):
        self.middle_name_date = message.text
        # Отправляем сообщение
        self.bot.reply_to(message, self.messagestouser.messagebirthdate,
                          reply_markup=self.buttonsmarkup.retunmarkup("Null"))
        self.bot.register_next_step_handler(message, self.town)

    # Добавление данных по городу
    def town(self, message):
        self.birth_date_date = message.text
        # Запрос к базе данных по имеющимся городам
        base = DataBase(pathtodatabase)
        req = "SELECT * FROM town ORDER BY name"
        # Полученные из базы данные
        dates = base.selectfromdatabase(req)
        # Формируем список всех городов
        towns = []
        for elem in dates:
            towns.append(elem[1])
        # Отправляем сообщение
        textmessage = self.bot.reply_to(message, self.messagestouser.messagechoosetown,
                            reply_markup=self.buttonsmarkup.retunmarkup("Города", towns))
        self.bot.register_next_step_handler(textmessage, self.type_sport)

    # Выбор типа спорта
    def type_sport(self, message):
        self.town_date_name = message.text

        # Проверка на отсутствие города в списке
        if message.text == "Моего варианта нету":
            self.town_date = None
            textmessageforadmin = "Клиент @" + str(message.from_user.username) + " не смог найти город. Надо связаться.\n"
            self.bot.send_message(self.tids.admin, textmessageforadmin)
        else:
            self.town_date = self.seart_id_in_database(message.text, "town")

        # Запрос к базе данных по имеющимся
        base = DataBase(pathtodatabase)
        req = "SELECT * FROM kind_sport ORDER BY name"
        # Полученные из базы данные
        dates = base.selectfromdatabase(req)
        # Формируем список всех видов спорта
        sports = []
        for elem in dates:
            sports.append(elem[1])
        # Отправляем сообщение
        textmessage = self.bot.reply_to(message, self.messagestouser.messagechoosetypesport,
                                        reply_markup=self.buttonsmarkup.retunmarkup("Тип спорта", sports))
        self.bot.register_next_step_handler(textmessage, self.level_training)

    # Выбор уровня подготовки
    def level_training(self, message):
        self.typesport_date_name = message.text

        # Проверка на отсутствие типа спорта в списке
        if message.text == "Моего варианта нету":
            self.typesport_date = None
            textmessageforadmin = "Клиент @" + str(message.from_user.username) + " не смог найти подходящий спорт. Надо связаться.\n"
            self.bot.send_message(self.tids.admin, textmessageforadmin)
        else:
            self.typesport_date = self.seart_id_in_database(message.text, "type_sport")

        # Запрос к базе данных по имеющимся городам
        base = DataBase(pathtodatabase)
        req = "SELECT * FROM level_training ORDER BY name"
        # Полученные из базы данные
        dates = base.selectfromdatabase(req)
        # Формируем список всех уровней
        levels = []
        for elem in dates:
            levels.append(elem[1])
        textmessage = self.bot.reply_to(message, self.messagestouser.messagechooselevel,
                                        reply_markup=self.buttonsmarkup.retunmarkup("Уровень", levels))

        self.bot.register_next_step_handler(textmessage, self.chooseplace)

    # Выбор места проведения тренировки
    def chooseplace(self, message):
        self.level_date_name = message.text
        self.level_date = self.seart_id_in_database(message.text, "level_training")
        # Запрос к базе данных по имеющимся городам
        base = DataBase(pathtodatabase)
        req = "SELECT * FROM place ORDER BY name"
        # Полученные из базы данные
        dates = base.selectfromdatabase(req)
        # Формируем список всех типов мест
        places = []
        for elem in dates:
            places.append(elem[1])
        textmessage = self.bot.reply_to(message, self.messagestouser.messagechooseplace,
                                        reply_markup=self.buttonsmarkup.retunmarkup("Места", places))

        self.bot.register_next_step_handler(textmessage, self.chooseType_accaunt)

    # Выбор типа аккаунта
    def chooseType_accaunt(self, message):
        self.place_date_name = message.text
        self.place_date = self.seart_id_in_database(message.text, "place")
        # Запрос к базе данных по имеющимся городам
        base = DataBase(pathtodatabase)
        req = "SELECT * FROM accaunt_type ORDER BY name"
        # Полученные из базы данные
        dates = base.selectfromdatabase(req)
        # Формируем список всех типов мест
        types = []
        for elem in dates:
            if elem[1] != "Администратор":
                types.append(elem[1])
        textmessage = self.bot.reply_to(message, self.messagestouser.messagechooseaccaunttype,
                                        reply_markup=self.buttonsmarkup.retunmarkup("Тип аккаунта", types))

        self.bot.register_next_step_handler(textmessage, self.descriptionfuncion)

    # Добавление описания к профилю
    def descriptionfuncion(self, message):
        self.accaunt_type_name = message.text
        self.accaunt_type = self.seart_id_in_database(message.text, "accaunt_type")
        # Отправляем сообщение
        self.bot.reply_to(message, self.messagestouser.messagedescription,
                          reply_markup=self.buttonsmarkup.retunmarkup("Null"))
        self.bot.register_next_step_handler(message, self.createfolderandsendphoto)

    # Добавление фотографии к профилю
    def createfolderandsendphoto(self, message):
        self.description_date = message.text
        # Создаём папку для пользователя
        pathdirectory = pathtoimagesusers + str(self.telegramid) + "/"
        if not os.path.exists(pathdirectory):
            os.makedirs(pathdirectory)
        # Отправляем сообщение
        self.bot.reply_to(message, self.messagestouser.messageimageuser,
                          reply_markup=self.buttonsmarkup.retunmarkup("Null"))
        self.bot.register_next_step_handler(message, self.sendalldatestoserver1, pathdirectory)

    # Сохранение картинки в папку
    def sendalldatestoserver1(self, message, path):
        # Обработка сохранения картинки на сервер
        image = message.photo[-1]
        fileinfo = self.bot.get_file(image.file_id)
        downloaded_file = self.bot.download_file(fileinfo.file_path)
        save_path = 'images/users/' + str(message.chat.id) + self.imagestouser.endpathprofile
        with open(save_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Отправляем сообщение
        self.bot.reply_to(message, self.messagestouser.messagefinalregistration,
                          reply_markup=self.buttonsmarkup.retunmarkup("Null"))

        messagetosenduser = "1. Фамилия Имя Отчество:\n          " + self.last_name_date + " " + self.first_name_date + " " + self.middle_name_date + "\n"
        messagetosenduser += "2. Возраст:\n          " + str(self.calc_age(self.birth_date_date)) + "\n"
        messagetosenduser += "3. Город:\n          " + str(self.town_date_name) + "\n"
        messagetosenduser += "4. Вид спорта:\n          " + str(self.typesport_date_name) + "\n"
        messagetosenduser += "5. Уровень подготовки:\n          " + str(self.level_date_name) + "\n"
        messagetosenduser += "6. Место проведения:\n          " + str(self.place_date_name) + "\n"
        messagetosenduser += "7. Тип аккаунта:\n          " + str(self.accaunt_type_name) + "\n"
        messagetosenduser += "8. Описание:\n          " + self.description_date + "\n\n"
        messagetosenduser += "⬇️Если всё ок, то нажми нажми внизу⬇️"

        # Формирование пути к фактографии
        pathurl = self.imagestouser.startpathprofile + str(self.telegramid) + self.imagestouser.endpathprofile

        self.bot.send_photo(message.chat.id, open(pathurl, 'rb'),
                            caption=messagetosenduser,
                            reply_markup=self.buttonsmarkup.retunmarkup("Отправить данные на сервер"))
        self.bot.register_next_step_handler(message, self.sendalldatestoserver2)

    # Записываем данные в базу данных
    def sendalldatestoserver2(self, message):
        if message.text == "Отправить данные на сервер":
            # Формируем данные для INSERT в базу данных
            insertdates = (self.first_name_date, self.middle_name_date, self.last_name_date, self.birth_date_date, self.raiting, self.telegramid,
                     self.town_date, self.typesport_date, self.level_date, self.typesport_date, self.place_date, self.description_date)
            # Добавление данных в базу данных
            # Подключаемся к базе данных
            connection = sqlite3.connect(self.pathdatabase)
            cursor = connection.cursor()
            # Запрос на добавление в таблицу
            request = "INSERT INTO users (first_name, middle_name, last_name, birth_date, rating, id_telegram, id_town, id_kind, id_level, id_type, id_place, description) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"
            cursor.execute(request, insertdates)
            connection.commit()
            connection.close()
            # Отправка сообщения, что данные успешно записаны
            self.bot.reply_to(message, self.messagestouser.messageinsertdatesindatabase,
                              reply_markup=self.buttonsmarkup.retunmarkup())
        else:
            # Отправка сообщения, что данные успешно записаны
            self.bot.reply_to(message, self.messagestouser.wrongcommand,
                              reply_markup=self.buttonsmarkup.retunmarkup())

    # Функция изменения профиля
    def editprofile(self, message, imagetouser, bot):
        print("Функция редактирования профиля")

        # Создаём кнопки для редактирования
        markup = telebot.types.InlineKeyboardMarkup()
        btnlastname = telebot.types.InlineKeyboardButton("Фамилия", callback_data = "lastname")
        markup.add(btnlastname)
        btnfirstname = telebot.types.InlineKeyboardButton("Имя", callback_data = "firstname")
        markup.add(btnfirstname)
        btnmiddlename = telebot.types.InlineKeyboardButton("Отчество", callback_data="middlename")
        markup.add(btnmiddlename)
        age = telebot.types.InlineKeyboardButton("Возраст", callback_data="age")
        markup.add(age)
        typesport = telebot.types.InlineKeyboardButton("Вид спорта", callback_data="typesport")
        markup.add(typesport)
        levelsport = telebot.types.InlineKeyboardButton("Уровень подготовки спорта", callback_data="levelsport")
        markup.add(levelsport)
        place = telebot.types.InlineKeyboardButton("Место проведения", callback_data="place")
        markup.add(place)
        typeaccaunt = telebot.types.InlineKeyboardButton("Тип аккаунта", callback_data="typeaccaunt")
        markup.add(typeaccaunt)
        discription = telebot.types.InlineKeyboardButton("Описание", callback_data="discription")
        markup.add(discription)

        # Отправляем сообщение пользователю
        bot.send_message(message.chat.id, "Что бы ты хотел поменять в своём профиле?", reply_markup=markup)

        # Функция выбора текста для отправки
        def choosetext(argument):
            match(argument):
                case ('lastname'):
                    text = "Хорошо. Введи пожалуйста новую Фамилию"
                case ('firstname'):
                    text = "Хорошо. Введи пожалуйста новую Имя"
                case ('middlename'):
                    text = "Хорошо. Введи пожалуйста новую Отчество"
                case ('age'):
                    text = "Хорошо. Введи пожалуйста новую Дату Рождения"
                case ('typesport'):
                    text = "Хорошо. Введи пожалуйста новый вид спорта"
                case('levelsport'):
                    text = "Хорошо. Введи пожалуйста свой новый уровень"
                case('place'):
                    text = "Хорошо. Введи пожалуйста новое место занятий"
                case('typeaccaunt'):
                    text = "Хорошо. Введи пожалуйста новый тип аккаунта"
                case('discription'):
                    text = "Хорошо. Введи пожалуйста новое описание"
                case _:
                    text = None
            return text

        # Функция генерации кнопок под категории которые выбираются.
        def choosemarkup(argument):
            # Создание меню
            #newmarkup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
            match (argument):
                case ('typesport'):
                    # Запрос к базе данных по имеющимся
                    base = DataBase(pathtodatabase)
                    req = "SELECT * FROM kind_sport ORDER BY name"
                    # Полученные из базы данные
                    dates = base.selectfromdatabase(req)
                    # Формируем список всех видов спорта
                    sports = []
                    for elem in dates:
                        sports.append(elem[1])
                    # Формируем кнопки
                    newmarkup = self.buttonsmarkup.retunmarkup("Тип спорта", sports)
                case ('levelsport'):
                    # Запрос к базе данных по имеющимся городам
                    base = DataBase(pathtodatabase)
                    req = "SELECT * FROM level_training ORDER BY name"
                    # Полученные из базы данные
                    dates = base.selectfromdatabase(req)
                    # Формируем список всех уровней
                    levels = []
                    for elem in dates:
                        levels.append(elem[1])
                    # Формируем кнопки
                    newmarkup = self.buttonsmarkup.retunmarkup("Уровень", levels)
                case ('place'):
                    # Запрос к базе данных по имеющимся городам
                    base = DataBase(pathtodatabase)
                    req = "SELECT * FROM place ORDER BY name"
                    # Полученные из базы данные
                    dates = base.selectfromdatabase(req)
                    # Формируем список всех типов мест
                    places = []
                    for elem in dates:
                        places.append(elem[1])
                    # Формируем кнопки
                    newmarkup = self.buttonsmarkup.retunmarkup("Уровень", places)
                case ('typeaccaunt'):
                    # Запрос к базе данных по имеющимся городам
                    base = DataBase(pathtodatabase)
                    req = "SELECT * FROM accaunt_type ORDER BY name"
                    # Полученные из базы данные
                    dates = base.selectfromdatabase(req)
                    # Формируем список всех типов аккаунтов
                    types = []
                    for elem in dates:
                        if elem[1] != "Администратор":
                            types.append(elem[1])
                    # Формируем кнопки
                    newmarkup = self.buttonsmarkup.retunmarkup("Уровень", types)
            return newmarkup

        @bot.callback_query_handler(func=lambda call: True)
        def callbackdata(call):
            # Выбор текста для отправки
            text = choosetext(call.data)
            markuptomessage = choosemarkup(call.data)
            if text == None:
                self.bot.answer_callback_query(callback_query_id=call.id, text="Что-то пошло не так(")
            # Отправляем сообщение пользователю
            replymessage = bot.send_message(message.chat.id, text, reply_markup=markuptomessage)
            bot.register_next_step_handler(replymessage, chengedata, call.data)

        # Функция выбора запроса для изменения данных
        def choosesql(argument, telegramid, mess):
            startsql = "UPDATE users SET "
            endsql = "WHERE id_telegram=" + str(telegramid)
            match (argument):
                case ('lastname'):
                    sql = startsql + "last_name='" + str(mess) + "' " + endsql
                case ('firstname'):
                    sql = startsql + "first_name='" + str(mess) + "' " + endsql
                case ('middlename'):
                    sql = startsql + "middle_name='" + str(mess) + "' " + endsql
                case ('age'):
                    sql = startsql + "birth_date='" + str(mess) + "' " + endsql
                case ('typesport'):
                    sql = startsql + "id_type='" + str(mess) + "' " + endsql
                case ('levelsport'):
                    sql = startsql + "id_level='" + str(mess) + "' " + endsql
                case ('place'):
                    sql = startsql + "id_place='" + str(mess) + "' " + endsql
                case ('typeaccaunt'):
                    sql = startsql + "id_type='" + str(mess) + "' " + endsql
                case ('discription'):
                    sql = startsql + "description='" + str(mess) + "' " + endsql
            return sql

        # Функция изменения данных
        def chengedata(message, data):
            sql = choosesql(data,  message.chat.id, message.text)
            # Подключаемся к базе данных
            connection = sqlite3.connect(self.pathdatabase)
            # Выполняем обновление в базе
            cursor = connection.cursor()
            cursor.execute(sql)
            connection.commit()
            # Закрываем соединение с базой
            connection.close()
            # Оповещаем пользователя, что всё удачно
            bot.send_message(message.chat.id, "Данные в базу записаны", reply_markup=self.buttonsmarkup.retunmarkup("Мой профиль"))

# Функция запроса к базе данных
def requestfordatabase(request, telegramid):
    # Запрос к базе данных
    base = DataBase(pathtodatabase)
    # Полученные из базы данные
    try:
        dates = base.selectfromdatabase(request)[0]
        return dates
    except:
        return None

# Вывод данный по существующему профилю
def selectdatesfromprofile(message, imagestouser, bot):
    telegramid = message.chat.id
    # Полученные из базы данные
    req = "SELECT * FROM users WHERE id_telegram=" + str(telegramid)
    dates = requestfordatabase(req, telegramid)

    # ФИО
    fio = dates[3] + " " + dates[1] + " " + dates[2]
    messagetosenduser = "1. Фамилия Имя Отчество:\n          " + str(fio) + "\n"

    # Возраст
    splitbirthdate = dates[4].split(".")
    intbirthdate = []
    # Преобразуем в чело численный тип и выставляем правильный порядок
    for elem in reversed(splitbirthdate):
        intbirthdate.append(int(elem))
    today = datetime.now().date()
    birthdatedate = date(intbirthdate[0], intbirthdate[1], intbirthdate[2])
    age = today.year - birthdatedate.year - ((today.month, today.day) < (birthdatedate.month, birthdatedate.day))
    messagetosenduser += "2. Возраст:\n          " + str(age) + "\n"

    # Рейтинг
    raiting = dates[5]
    messagetosenduser += "3. Рейтинг в системе:\n          " + str(raiting) + "\n"

    # Город
    req = "SELECT name FROM town, users where users.id_town = town.id_town AND users.id_telegram=" + str(telegramid)
    town = requestfordatabase(req, telegramid)
    if town == None:
        messagetosenduser += "4. Город:\n          Не выбран \n"
    else:
        messagetosenduser += "4. Город:\n          " + str(town[0]) + "\n"

    # Вид спорта
    req = "SELECT name FROM kind_sport, users where users.id_kind=kind_sport.id_kind AND users.id_telegram=" + str(telegramid)
    kind_sport = requestfordatabase(req, telegramid)
    if kind_sport == None:
        messagetosenduser += "5. Вид спорта:\n          Не выбран \n"
    else:
        messagetosenduser += "5. Вид спорта:\n          " + str(kind_sport[0]) + "\n"

    # Уроверь подготовки
    req = "SELECT name FROM level_training, users where users.id_level=level_training.id_level AND users.id_telegram=" + str(telegramid)
    level_training = requestfordatabase(req, telegramid)
    if level_training == None:
        messagetosenduser += "6. Уровень подготовки:\n          Не выбран \n"
    else:
        messagetosenduser += "6. Уровень подготовки:\n          " + str(level_training[0]) + "\n"

    # Место проведения
    req = "SELECT name FROM place, users where users.id_place=place.id_place AND users.id_telegram=" + str(telegramid)
    training_place = requestfordatabase(req, telegramid)
    if training_place == None:
        messagetosenduser += "7. Место проведения:\n          Не выбран \n"
    else:
        messagetosenduser += "7. Место проведения:\n          " + str(training_place[0]) + "\n"

    # Тип аккаунта
    req = "SELECT name FROM accaunt_type, users where users.id_place=accaunt_type.id_type AND users.id_telegram=" + str(telegramid)
    accaunt_type = requestfordatabase(req, telegramid)
    if accaunt_type == None:
        messagetosenduser += "8. Тип аккаунта:\n          Не выбран \n"
    else:
        messagetosenduser += "8. Тип аккаунта:\n          " + str(accaunt_type[0]) + "\n"

    description = dates[12]

    messagetosenduser += "9. Описание:\n          " + str(description)

    # Формирование пути к фактографии
    pathtoimage = imagestouser.startpathprofile + str(telegramid) + "/profile.png"

    # Отправка профиля
    bot.send_photo(message.chat.id, photo=open(pathtoimage, 'rb'),
                   caption=messagetosenduser)