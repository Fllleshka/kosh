from datetime import *

from telebot.types import PreparedInlineMessage
from urllib3 import request

from classes.imports import *

# Импорт библиотеки для работы с ботом
import telebot
import json

class profile:
    # Инициализация переменных
    def __init__(self, bot, messagestouser, buttonsmarkup):
        self.bot = bot
        self.messagestouser = messagestouser
        self.buttonsmarkup = buttonsmarkup
        self.fulldates = []

        self.first_name_date = ""
        self.last_name_date = ""
        self.middle_name_date = ""
        self.age = ""
        self.raiting = ""
        self.telegramid = None
        self.town_date = ""
        self.typesport_date = ""
        self.level_date = ""
        self.description_date = ""
        self.place_date = ""
        self.description = ""

    # Вывод всех данных
    def printdates(self):
        print("==================")
        print(f"Имя: \t\t\t\t{self.first_name_date}")
        print(f"Фамилия: \t\t\t{self.last_name_date}")
        print(f"Отчество: \t\t\t{self.middle_name_date}")
        print(f"Возраст: \t\t\t{self.age}")
        print(f"Рейтинг: \t\t\t{self.raiting}")
        print(f"TelegramID: \t\t{self.telegramid}")
        print(f"Город: \t\t\t\t{self.town_date}")
        print(f"Вид спорта: \t\t\t{self.typesport_date}")
        print(f"Уровень подготовки: \t{self.level_date}")
        print(f"Тип учётной записи: \t{self.description_date}")
        print(f"Место проведения: \t{self.place_date}")
        print(f"Описание: {self.description}")
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
        self.raiting = 0
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
        self.age = self.calc_age(message.text)
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
        self.town_date = message.text
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

    # Выбор типа спорта
    def level_training(self, message):
        self.typesport_date = message.text
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
        self.level_date = message.text
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

        self.bot.register_next_step_handler(textmessage, self.descriptionfuncion)

    # Добавление описания к профилю
    def descriptionfuncion(self, message):
        self.place_date = message.text
        # Отправляем сообщение
        self.bot.reply_to(message, self.messagestouser.messagedescription,
                          reply_markup=self.buttonsmarkup.retunmarkup("Null"))
        self.bot.register_next_step_handler(message, self.sendalldatestoserver)

    # Отправка данных на сервер
    def sendalldatestoserver(self, message):
        self.description_date = message.text
        self.printdates()