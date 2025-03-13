# Токен для бота
tokenbot = "7812465689:AAHP_i1P6zoh8_0Q_d_-ec-5_pYNzmtpEe0"

# Путь к базе данных:
pathtodatabase = "database/maindatabase.db"

# Путь к папке с фотографиями пользователей
pathtoimagesusers = "images/users/"

# Путь к телеграмм каналу: Надо заменить ссылку!
telegrampath = "https://t.me/Wylsared"

# Путь к администратору канала:
adminchannel = "https://telegram.org/@fleshkaomsk"

# Класс картинок
class images:
    def __init__(self):
        # Стартовая картинка в приветственном сообщении
        self.startimage = "images/startimage.png"
        # Первоначальная картинка каждого профиля
        self.startuserimage = "images/startimage.png"
        # Путь к папке с файлами профилей
        self.startpathprofile = "images/users/"
        # Название картинки в профиле
        self.endpathprofile = "/profile.png"

# Класс сообщений
class messages:
    def __init__(self):
        # Приветственное сообщение
        self.welcomemessage = "Привет!\nДобро пожаловать в спортивное сообщество Kosh Sports.\nЗдесь спортсмены находят себе единомышленников и лучших тренеров, а тренеры находят талантливых учеников.\nА кто ты?"
        # Неверное сообщение
        self.wrongcommand = "Не понимаю команду("
        # Сообщание интересующимся телеграмм каналом
        self.interestinginfo = "В таком случае, рекомендуем подписаться на наш телеграмм канал.\nТам мы выкладываем всю актуальную информацию, а так же будем рады видеть тебя на канале"
        # Сообщение первичное для профиля тренера
        self.messagecoachstart = "Отлично!😃\nДавай заполни твой профиль, чтобы спортсмены могли найти тебя!😎"
        # Сообщение вторичное для ввода имени тренера
        self.messagecoachfirstname = "Введи своё Имя"
        # Сообщение вторичное для ввода фамилии тренера
        self.messagecoachlastname = "Введи свою Фамилию"
        # Сообщение вторичное для ввода фамилии тренера
        self.messagecoachmiddlename = "Введи своё Отчество"
        # Сообщение для ввода даты рождения
        self.messagebirthdate = "Введи свою Дату рождения в формате:\n'01.01.2025'"
        # Сообщение для ввода города
        self.messagechoosetown = "Выбери свой город из списка внизу"
        # Сообщение для ввода типа спорта
        self.messagechoosetypesport = "Выбери свой спорт из списка внизу"
        # Сообщение для ввода уровня спортсмена
        self.messagechooselevel = "Выбери свой уровень"
        # Сообщение для ввода типа помещения
        self.messagechooseplace = "Выбери место где будем тренироваться"
        # Сообщение для ввода типа аккаунта
        self.messagechooseaccaunttype = "Выбери тип аккаунта"
        # Сообщение для отправки фотографии аккаунта
        self.messageimageuser = "Отправь мне свою фотографию, чтобы прикрепить её к профилю"
        # Сообщение для ввода описания к анкете
        self.messagedescription = "Напиши пожалуйста небольшое описание, к своей анкете"
        # Сообщение для ввода описания к анкете
        self.messagefinalregistration = "Отлично!\nДавай посмотрим что мы сделали."
        # Сообщения для успешной записи в базу данных
        self.messageinsertdatesindatabase = "Поздравляю, ты теперь вместе с нами!"
        # Сообщение о том что такой профиль уже найден в базе данных
        self.messageprofilealreadyexists = "Друг, твой профиль уже есть в системе."


# Класс данных по админам:
class telegramids:
    def __init__(self):
        self.founder1 = None
        self.founder2 = None
        self.admin = 1917167694