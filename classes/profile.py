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
    def __init__(self, bot, messagestouser, buttonsmarkup, imagestouser):
        self.bot = bot
        self.pathdatabase = pathtodatabase
        self.messagestouser = messagestouser
        self.buttonsmarkup = buttonsmarkup
        self.imagestouser = imagestouser
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
        # Определяем telegramId
        self.telegramid = message.chat.id
        print(self.telegramid)
        # Запрос со всеми telegramid которые есть в базе
        base = DataBase(pathtodatabase)
        request = "SELECT id_telegram FROM users"
        # Полученные из базы данные
        dates = base.selectfromdatabase(request)
        # Формируем список всех типов мест
        print(dates)

        # Если такой id есть в системе возвращаем True
        if self.telegramid == 1871580124:
            return True

        else:
            return False

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

    # Добавление даты рождения для тренера
    def birth_date(self, message):
        self.middle_name_date = message.text
        # Отправляем сообщение
        self.bot.reply_to(message, self.messagestouser.messagebirthdate,
                          reply_markup=self.buttonsmarkup.retunmarkup("Null"))
        self.bot.register_next_step_handler(message, self.town)

    # Добавление данных по
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
        self.typesport_date = self.seart_id_in_database(message.text, "type_sport")
        # Запрос к базе данных по имеющимся городам
        base = DataBase(pathtodatabase)
        req = "SELECT * FROM level_training ORDER BY name"
        # Полученные из базы данные
        dates = base.selectfromdatabase(req)
        # Формируем список всех городов
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
        print(message.chat.id)
        print(type(message.chat.id))
        save_path = 'images/users/' + str(message.chat.id) + "/profile.png"
        with open(save_path, 'wb') as new_file:
            new_file.write(downloaded_file)

        # Отправляем сообщение
        self.bot.reply_to(message, self.messagestouser.messagefinalregistration,
                          reply_markup=self.buttonsmarkup.retunmarkup("Null"))
        self.printdates()

        messagetosenduser = "1. Фамилия Имя Отчество:\n          " + self.last_name_date + " " + self.first_name_date + " " + self.middle_name_date + "\n"
        messagetosenduser += "2. Возраст:\n          " + str(self.calc_age(self.birth_date_date)) + "\n"
        messagetosenduser += "3. Город:\n          " + str(self.town_date_name) + "\n"
        messagetosenduser += "4. Вид спорта:\n          " + str(self.typesport_date_name) + "\n"
        messagetosenduser += "5. Уровень подготовки:\n          " + str(self.level_date_name) + "\n"
        messagetosenduser += "6. Место проведения:\n          " + str(self.place_date_name) + "\n"
        messagetosenduser += "7. Тип аккаунта:\n          " + str(self.accaunt_type_name) + "\n"
        messagetosenduser += "8. Описание:\n          " + self.description_date + "\n\n"
        messagetosenduser += "⬇️Если всё ок, то нажми нажми внизу⬇️"

        self.bot.send_photo(message.chat.id, open(self.imagestouser.startuserimage, 'rb'),
                            caption=messagetosenduser,
                            reply_markup=self.buttonsmarkup.retunmarkup("Отправить данные на сервер"))
        self.bot.register_next_step_handler(message, self.sendalldatestoserver2)

    # Записываем данные в базу данных
    def sendalldatestoserver2(self,message):
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
                          reply_markup=self.buttonsmarkup.retunmarkup("Null"))