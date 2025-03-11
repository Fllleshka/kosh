from telebot.apihelper import download_file

from classes.imports import *

# Запуск программы проверка файлов
if __name__ == "__main__":
    # Инициализация значений
    data = DataBase(pathtodatabase)
    # Если файл базы данных существует
    if (data.checkfiledatabase() == True):
        pass
    # Если нет, то инициализируем базу
    else:
        data.createdatabase()
        data.inittables()

# Приветственное сообщение (обработка кнопки /start)
@bot.message_handler(commands=['start'])
def startmessage(message):
    # Отправка сообщения
    bot.send_photo(message.chat.id, photo=open(imagestouser.startimage, 'rb'),
                   caption=messagestouser.welcomemessage,
                   reply_markup = buttonsmarkup.retunmarkup())

# Обработка отправленного текста (кнопки)
@bot.message_handler(content_types= ['text'])
def textmessage(message):
    match (message.text):
        case "💪Я тренер💪":
            bot.send_message(message.chat.id, "Отлично работаем дальше",
                             reply_markup = buttonsmarkup.retunmarkup("Тренер"))
        case "🏅Я спортсмен🏅":
            bot.send_message(message.chat.id, "Отлично работаем дальше",
                             reply_markup=buttonsmarkup.retunmarkup("Спортсмен"))
        case "🧐Я просто интересуюсь🧐" | "Получить полезную информацию о спорте":
            bot.send_message(message.chat.id, messagestouser.interestinginfo,
                             reply_markup=buttonsmarkup.retunmarkup("Ссылка на канал"))
        case "Мой профиль 💪":
            # Инициалзиация класса отвечающего за профиль
            profileinf = profile(bot, messagestouser, buttonsmarkup, imagestouser)
            # Проверка на существование профиля в базе данных
            if (profileinf.existencecheck(message) == False):
                profileinf.first_name(message)
            else:
                bot.send_message(message.chat.id, messagestouser.messageprofilealreadyexists,
                                 reply_markup=buttonsmarkup.retunmarkup("Отредактировать профиль"))
        case "Поехали заполнять":
            bot.send_message(message.chat.id, messagestouser.messagecoachstart,
                     reply_markup=buttonsmarkup.retunmarkup("Профиль тренера"))
        case "Найти тренера":
            bot.register_next_step_handler(message, searchprof.printdates)

        case "Моего варианта нету":
            bot.send_message(message.chat.id, "Напиши мне и мы добавим!",
                     reply_markup=buttonsmarkup.retunmarkup("Добавление данных"))
        case _:
            bot.reply_to(message, messagestouser.wrongcommand, reply_markup = buttonsmarkup.retunmarkup())

# Запуск бесконечного опроса
bot.infinity_polling()