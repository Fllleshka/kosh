from classes.imports import *

# Импорт библиотеки для работы с ботом
import telebot

# Кнопки
class buttons:
    # Инициализация класса
    def __init__(self):
        self.btn1 = telebot.types.KeyboardButton("💪Я тренер💪")
        self.btn2 = telebot.types.KeyboardButton("🏅Я спортсмен🏅")
        self.btn3 = telebot.types.KeyboardButton("Внести данные в анкету")


    def retunmarkup(self, role=None):
        # Создание меню
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        match (role):
            case _:
                markup.add(self.btn1)
                markup.add(self.btn2)
        return markup