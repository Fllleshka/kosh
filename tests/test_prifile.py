from classes.imports import *

class profileTestCase():
    def testprintdates(self):
        # Инициализация бота
        bot = telebot.TeleBot(tokenbot)
        # Инициализация кнопок
        buttonsmarkup = buttons()
        # Инициализация сообщений
        messagestouser = messages()
        # Инициализация экземпляра класса
        testclass = profile(bot, messagestouser, buttonsmarkup)
        # Параметры для функции printdates
        testclass.printdates()

test = profileTestCase()
test.testprintdates()