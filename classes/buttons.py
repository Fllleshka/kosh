from classes.imports import *

# Импорт библиотеки для работы с ботом
import telebot

# Кнопки
class buttons:
    # Инициализация класса
    def __init__(self):
        self.btn1 = telebot.types.KeyboardButton("💪Я тренер💪")
        self.btn2 = telebot.types.KeyboardButton("🏅Я спортсмен🏅")
        self.btn3 = telebot.types.KeyboardButton("🧐Я просто интересуюсь🧐")
        self.btn4 = telebot.types.KeyboardButton("Найти тренера")
        self.btn6 = telebot.types.KeyboardButton("Найти партнёра для занятий спортом")
        self.btn7 = telebot.types.KeyboardButton("Принять участие в соревнованиях")
        self.btn8 = telebot.types.KeyboardButton("Получить полезную информацию о спорте")
        self.btn9 = telebot.types.KeyboardButton("Мой профиль 💪")
        self.btn10 = telebot.types.KeyboardButton("Найти спортсмена")
        self.btn11 = telebot.types.KeyboardButton("Моего варианта нету")
        self.btn12 = telebot.types.KeyboardButton("Мой профиль для других")


        self.btntelegramchannel = telebot.types.InlineKeyboardButton("Kosh Sports", telegrampath)
        self.sendinformation = telebot.types.KeyboardButton("Отправить данные на сервер")
        self.changeprofileinfo = telebot.types.KeyboardButton("Отредактировать профиль")
        self.sendmessageadmin = telebot.types.InlineKeyboardButton("Админ", adminchannel)

    def retunmarkup(self, role=None, dates=None):
        # Создание меню
        markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
        match (role):

            case "Тренер":
                markup.add(self.btn9)
                markup.add(self.btn10)
                markup.add(self.btn7)

            case "Спортсмен":
                markup.add(self.btn9)
                markup.add(self.btn4)
                markup.add(self.btn6)
                markup.add(self.btn7)

            case "Ссылка на канал":
                markup = telebot.types.InlineKeyboardMarkup()
                markup.add(self.btntelegramchannel)

            case "Профиль тренера":
                markup.add(self.btn10)

            case "Null":
                markup = telebot.types.ReplyKeyboardRemove()

            case "Города" | "Тип спорта":
                for elem in range(0, len(dates), 2):
                    # Обработка нечётного количества элементов в массиве
                    if len(dates) % 2 == 1:
                        if elem == (len(dates) // 2) * 2:
                            button = telebot.types.KeyboardButton(dates[elem])
                            markup.add(button)
                        else:
                            button1 = telebot.types.KeyboardButton(dates[elem])
                            button2 = telebot.types.KeyboardButton(dates[elem+1])
                            markup.add(button1, button2)
                    else:
                        button1 = telebot.types.KeyboardButton(dates[elem])
                        button2 = telebot.types.KeyboardButton(dates[elem + 1])
                        markup.add(button1, button2)
                markup.add(self.btn11)

            case "Уровень" | "Места" | "Тип аккаунта":
                for elem in dates:
                    markup.add(elem)

            case "Отправить данные на сервер":
                markup.add(self.sendinformation)

            case "Мой профиль":
                markup.add(self.btn12)
                markup.add(self.changeprofileinfo)

            case "Добавление данных":
                markup = telebot.types.InlineKeyboardMarkup()
                markup.add(self.btntelegramchannel)

            case _:
                markup.add(self.btn1)
                markup.add(self.btn2)
                markup.add(self.btn3)
        return markup