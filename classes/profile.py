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
    # Добавление имя для тренера
    def first_name(self, message):
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
        print(f"{self.first_name_date} {self.middle_name_date} {self.last_name_date}")

