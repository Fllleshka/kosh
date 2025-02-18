from datetime import *

from telebot.types import PreparedInlineMessage

from classes.imports import *

# Импорт библиотеки для работы с ботом
import telebot
import json

class profile:
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
        self.description = ""
        self.town_date = ""
        self.typesport_date = ""
        self.level_date = ""
        self.description_date = ""
        self.place_date = ""

    # Вывод всех данных
    def printdates(self):
        testdatetime = "09.08.1997"
        print("==================")
        print(f"Имя: \t\t{self.first_name_date}")
        print(f"Фамилия: \t{self.last_name_date}")
        print(f"Отчество: \t{self.middle_name_date}")
        print(f"Возраст: {self.calc_age(testdatetime)}")
        print(f"Рейтинг: {self.raiting}")
        print(f"TelegramID: \t{self.telegramid}")
        print(f"Город: \t{self.town_date}")
        print(f"Вид спорта: \t{self.typesport_date}")
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

    # Добавление имя для тренера
    def first_name(self, message):
        # Определяем telegramId
        self.telegramid = message.chat.id
        # Отправляем сообщение
        self.bot.reply_to(message, self.messagestouser.messagecoachfirstname,
                            reply_markup=self.buttonsmarkup.retunmarkup("Null"))
        self.bot.register_next_step_handler(message, self.last_name)

    # Добавление фамилия для тренера
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

    # Добавление даты рождения для тренера
    def town(self, message):
        self.town_date = message.text