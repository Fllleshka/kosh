import os
import sqlite3

class DataBase:
    # Инициализация пути к базе данных
    def __init__(self, path):
        self.pathdatabase = path

    # Проверка на существование файла базы данных
    def checkfiledatabase(self):
        if (os.path.exists(self.pathdatabase) == True):
            print(f"Файл [{self.pathdatabase}] существует")
            return True
        else:
            print(f"Файл [{self.pathdatabase}] не существует")
            return False

    # Создание файла базы данных
    def createdatabase(self):
        file = open(self.pathdatabase, "w+")
        file.close()
        print("Файл базы данных успешно создан")

    # Инициализация таблиц в базе данных
    def inittables(self):
        # Подключаемся к базе данных
        connection = sqlite3.connect(self.pathdatabase)
        cursor = connection.cursor()

        # Создаём таблицу town
        cursor.execute('''
            CREATE TABLE town(
                id_town INTEGER PRIMARY KEY AUTOINCREMENT,
                name varchar(255) NOT NULL)
        ''')
        connection.commit()

        # Создаём таблицу sport_kind
        cursor.execute('''
            CREATE TABLE kind_sport(
                id_kind INTEGER PRIMARY KEY AUTOINCREMENT,
                name varchar(255) NOT NULL)
        ''')
        connection.commit()

        # Создаём таблицу level_training
        cursor.execute('''
                    CREATE TABLE level_training(
                        id_level INTEGER PRIMARY KEY AUTOINCREMENT,
                        name varchar(255) NOT NULL)
                ''')
        connection.commit()


        # Создаём таблицу accaunt_type
        cursor.execute('''
                    CREATE TABLE accaunt_type(
                        id_type INTEGER PRIMARY KEY AUTOINCREMENT,
                        name varchar(255) NOT NULL)
                ''')
        connection.commit()

        # Создаём таблицу place
        cursor.execute('''
                            CREATE TABLE place(
                                id_place INTEGER PRIMARY KEY AUTOINCREMENT,
                                name varchar(255) NOT NULL)
                        ''')
        connection.commit()

        # Создаём таблицу users
        cursor.execute('''
                    CREATE TABLE users(
                        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
                        first_name varchar(255) NOT NULL,
                        middle_name varchar(255),
                        last_name varchar(255) NOT NULL,
                        birth_date TEXT,
                        rating INTEGER DEFAULT 0,
                        id_telegram INTEGER,
                        id_town INTEGER,
                        id_kind INTEGER,
                        id_level INTEGER,
                        id_type INTEGER,
                        id_place INTEGER,
                        description TEXT,
                        FOREIGN KEY (id_town) REFERENCES town (id_town) ON DELETE SET NULL,
                        FOREIGN KEY (id_kind) REFERENCES kind_sport (id_kind) ON DELETE SET NULL,
                        FOREIGN KEY (id_level) REFERENCES level_training (id_level) ON DELETE SET NULL,
                        FOREIGN KEY (id_type) REFERENCES accaunt_type (id_type) ON DELETE SET NULL,
                        FOREIGN KEY (id_place) REFERENCES place (id_place) ON DELETE SET NULL
                        )
                        ''')
        connection.commit()

        # Закрываем соединение с базой
        connection.close()

        # Вызываем функцию заполения базы тестовыми данными
        self.inserttestdatesintodatabase()

    # Функция выполнения запроса на вывод данных (SELECT) к базе
    def selectfromdatabase(self, request):
        # Подключаемся к базе данных
        connection = sqlite3.connect(self.pathdatabase)
        cursor = connection.cursor()
        # Выполнение запроса
        cursor.execute(request)
        result = cursor.fetchall()
        # Закрываем соединение с базой
        connection.close()
        # Возвращаем данные
        return result

    # Функция выполнения запроса на добавление данных (INSERT) к базе
    def insertintodatabase(self, request):
        # Подключаемся к базе данных
        connection = sqlite3.connect(self.pathdatabase)
        cursor = connection.cursor()
        # Выполнение запроса
        cursor.execute(request)
        result = cursor.commit()
        # Закрываем соединение с базой
        connection.close()
        # Возвращаем данные
        return result

    # Функция наполнения базы данных тестовыми данными:
    def inserttestdatesintodatabase(self):
        # Подключаемся к базе данных
        connection = sqlite3.connect(self.pathdatabase)
        cursor = connection.cursor()

        # Заполнение таблицы town
        cursor.execute('''
                    INSERT INTO town(
                        name)
                        VALUES
                        ('Омск'), ('Томск'), ('Москва'), ('Новосибирск'), ('Санкт-Петербург'), ('Сочи'), ('Калининград'),
                        ('Владивосток'), ('Екатеринбург'), ('Казань'), ('Красноярск'), ('Нижний Новгород'), ('Уфа'),
                        ('Самара'), ('Ростов-на-Дону'), ('Краснодар'), ('Пермь'), ('Воронеж')
                        ''')
        connection.commit()

        # Заполнение таблицы kind_sport
        cursor.execute('''
                            INSERT INTO kind_sport(
                                name)
                                VALUES
                                ('Бег'), ('Футбол'), ('Баскетбол'), ('Бокс'), ('Велоспорт'), ('Волейбол'), ('Гольф'),
                                ('Горные лыжи'), ('Дзюдо'), ('Киберспорт'), ('Коньки'), ('Легкая атлетика'), ('Настольный теннис'),
                                ('Плавание'), ('Триатлон'), ('Хоккей'), ('Шахматы')
                                ''')
        connection.commit()

        # Заполнение таблицы level_training
        cursor.execute('''
                    INSERT INTO level_training(
                        name)
                        VALUES
                        ('Любитель'), ('Начинающий'), ('Профессионал')
                        ''')
        connection.commit()

        # Заполнение таблицы accaunt_type
        cursor.execute('''
                    INSERT INTO accaunt_type(
                        name)
                        VALUES
                        ('Тренер'), ('Спортсмен'), ('Администратор')
                        ''')
        connection.commit()

        # Заполнение таблицы place
        cursor.execute('''
                            INSERT INTO place(
                                name)
                                VALUES
                                ('Спортивный клуб/зал'), ('Улица'), ('Онлайн'), ('В любом месте')
                                ''')
        connection.commit()

        # Заполнение таблицы users
        # Фетисов Денис Елисеевич
        cursor.execute('''
                            INSERT INTO users(
                                first_name, middle_name, last_name,
                                birth_date, rating, id_telegram,
                                id_town, id_kind, id_level,
                                id_type, id_place, description)
                                VALUES
                                (('Денис'), ('Елисеевич'), ('Фетисов'),
                                ('17.01.1998'), ('43'), ('None'),
                                ('3'), ('1'), ('1'),
                                ('2'), ('2'),
                                ('Всем привет! Хочу бегать короткие дистанции до 1 км. Пишите станцию метро в сообщении, чтобы сразу найтись)'))
                                ''')
        connection.commit()
        # Иванова Виктория Михайловна
        cursor.execute('''
                            INSERT INTO users(
                                first_name, middle_name, last_name,
                                birth_date, rating, id_telegram,
                                id_town, id_kind, id_level,
                                id_type, id_place, description)
                                VALUES
                                (('Виктория'), ('Михайловна'), ('Иванова'),
                                ('03.11.2001'), ('13'), ('None'),
                                ('3'), ('1'), ('1'),
                                ('2'), ('2'),
                                ('Занимаюсь спортом в удовольствие) Бегаю не на результат) Пишите :D'))
                                ''')
        connection.commit()
        # Новиков Владимир Ильич
        cursor.execute('''
                            INSERT INTO users(
                                first_name, middle_name, last_name,
                                birth_date, rating, id_telegram,
                                id_town, id_kind, id_level,
                                id_type, id_place, description)
                                VALUES
                                (('Владимир'), ('Ильич'), ('Новиков'),
                                ('17.04.2005'), ('117'), ('None'),
                                ('3'), ('1'), ('3'),
                                ('2'), ('2'),
                                ('Моя цель выбежать из 14 минут на дистанции 5 километров. Присоединяйтесь, кто сможет удержать темп!'))
                                ''')
        connection.commit()
        # Березина Анна Ярославовна
        cursor.execute('''
                            INSERT INTO users(
                                first_name, middle_name, last_name,
                                birth_date, rating, id_telegram,
                                id_town, id_kind, id_level,
                                id_type, id_place, description)
                                VALUES
                                (('Анна'), ('Ярославовна'), ('Березина'),
                                ('03.12.2001'), ('117'), ('None'),
                                ('3'), ('1'), ('1'),
                                ('2'), ('2'),
                                ('Новые знакомства в беге, это прекрасно! Надеюсь найти новых друзей...'))
                                ''')
        connection.commit()
        # Голубев Алексей Филиппович
        cursor.execute('''
                            INSERT INTO users(
                                first_name, middle_name, last_name,
                                birth_date, rating, id_telegram,
                                id_town, id_kind, id_level,
                                id_type, id_place, description)
                                VALUES
                                (('Алексей'), ('Филиппович'), ('Голубев'),
                                ('19.02.1990'), ('401'), ('None'),
                                ('5'), ('17'), ('3'),
                                ('1'), ('3'),
                                ('Мастер спорта по шахматам к вашим услугам. Обучаю как профессионалов, так и начинающих.'))
                                ''')
        connection.commit()
        # Павлова Екатерина Тимофеевна
        cursor.execute('''
                            INSERT INTO users(
                                first_name, middle_name, last_name,
                                birth_date, rating, id_telegram,
                                id_town, id_kind, id_level,
                                id_type, id_place, description)
                                VALUES
                                (('Екатерина'), ('Тимофеевна'), ('Павлова'),
                                ('10.05.1996'), ('23'), ('None'),
                                ('6'), ('8'), ('1'),
                                ('2'), ('2'),
                                ('Познакомлюсь с прекрасным парнем для раскатывания паудера и фрирайда. '))
                                ''')
        connection.commit()
        # Краснов Денис Никитич
        cursor.execute('''
                            INSERT INTO users(
                                first_name, middle_name, last_name,
                                birth_date, rating, id_telegram,
                                id_town, id_kind, id_level,
                                id_type, id_place, description)
                                VALUES
                                (('Денис'), ('Никитич'), ('Краснов'),
                                ('18.12.2006'), ('7'), ('None'),
                                ('3'), ('14'), ('1'),
                                ('2'), ('1'),
                                ('Хочу стать мастером спорта по плаванию. В поисках наставника для совершенствования'))
                                ''')
        connection.commit()
        # Ершова Варвара Тимуровна
        cursor.execute('''
                            INSERT INTO users(
                                first_name, middle_name, last_name,
                                birth_date, rating, id_telegram,
                                id_town, id_kind, id_level,
                                id_type, id_place, description)
                                VALUES
                                (('Варвара'), ('Тимуровна'), ('Ершова'),
                                ('01.01.2001'), ('19'), ('None'),
                                ('3'), ('1'), ('1'),
                                ('2'), ('2'),
                                ('Пишите'))
                                ''')
        connection.commit()
        # Андреев Даниил Тимофеевич
        cursor.execute('''
                            INSERT INTO users(
                                first_name, middle_name, last_name,
                                birth_date, rating, id_telegram,
                                id_town, id_kind, id_level,
                                id_type, id_place, description)
                                VALUES
                                (('Даниил'), ('Тимофеевич'), ('Андреев'),
                                ('27.11.2000'), ('0'), ('None'),
                                ('3'), ('1'), ('1'),
                                ('2'), ('2'),
                                ('Добрый день. Бегаю каждое утро в 06:00. Нужна компания для ранних пробежек'))
                                ''')
        connection.commit()
        # Зуева Малика Дмитриевна
        cursor.execute('''
                            INSERT INTO users(
                                first_name, middle_name, last_name,
                                birth_date, rating, id_telegram,
                                id_town, id_kind, id_level,
                                id_type, id_place, description)
                                VALUES
                                (('Малика'), ('Дмитриевна'), ('Зуева'),
                                ('01.12.2004'), ('21'), ('None'),
                                ('3'), ('1'), ('1'),
                                ('2'), ('2'),
                                ('Вечерние пробежки по набережной. Присоединяйтесь)'))
                                ''')
        connection.commit()

        # Закрываем соединение с базой
        connection.close()