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


    sql = "SELECT * FROM town"
    print(data.selectfromdatabase(sql))

# Приветственное сообщение (обработка кнопки /start)
@bot.message_handler(commands=['start'])
def startmessage(message):
    # Отправка сообщения
    bot.send_photo(message.chat.id, photo=open(imagestouser.startimage, 'rb'), caption=messagestouser.welcomemessage, reply_markup = buttonsmarkup.retunmarkup())

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
        case "🧐Я просто интересуюсь🧐":
            bot.send_message(message.chat.id, messagestouser.interestinginfo,
                             reply_markup=buttonsmarkup.retunmarkup("Ссылка на канал"))
        case "Получить полезную информацию о спорте":
            bot.send_message(message.chat.id, messagestouser.interestinginfo,
                     reply_markup=buttonsmarkup.retunmarkup("Ссылка на канал"))
        case _:
            bot.reply_to(message, messagestouser.wrongcommand, reply_markup = buttonsmarkup.retunmarkup())

# Запуск бесконечного опроса
bot.infinity_polling()