# Токен для бота
tokenbot = "7812465689:AAHP_i1P6zoh8_0Q_d_-ec-5_pYNzmtpEe0"

# Путь к базе данных:
pathtodatabase = "database/maindatabase.db"

# Класс картинок
class images:
    def __init__(self):
        #Стартовая картинка в приветсвтенном сообщении
        self.startimage = "images/startimage.png"

# Класс сообщений
class messages:
    def __init__(self):
        # Приветственное сообщение
        self.welcomemessage = "Привет!\nДобро пожаловать в спортивное сообщество Kosh Sports.\nЗдесь спортсмены находят себе единомышленников и лучших тренеров, а тренеры находят талантливых учеников.\nА кто ты?"
        # Неверное сообщение
        self.wrongcommand = "Не понимаю команду("