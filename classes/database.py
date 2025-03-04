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
        # Заполнение таблицы
        cursor.execute('''
            INSERT INTO town(
                name)
                VALUES
                ('Омск'), ('Томск'), ('Москва'), ('Новосибирск'), ('Санкт-Петербург'), ('Сочи'), ('Калининград'),
                ('Владивосток'), ('Екатеринбург'), ('Казань'), ('Красноярск'), ('Нижний Новгород'), ('Уфа'),
                ('Самара'), ('Ростов-на-Дону'), ('Краснодар'), ('Пермь'), ('Нижний Воронеж')
                ''')
        connection.commit()

        # Создаём таблицу sport_kind
        cursor.execute('''
            CREATE TABLE kind_sport(
                id_kind INTEGER PRIMARY KEY AUTOINCREMENT,
                name varchar(255) NOT NULL)
        ''')
        connection.commit()
        # Заполнение таблицы
        cursor.execute('''
                    INSERT INTO kind_sport(
                        name)
                        VALUES
                        ('Бег'), ('Футбол'), ('Баскетбол'), ('Бокс'), ('Велоспорт'), ('Волейбол'), ('Гольф'),
                        ('Горные лыжи'), ('Дзюдо'), ('Киберспорт'), ('Коньки'), ('Легкая атлетика'), ('Настольный теннис'),
                        ('Плавание'), ('Триатлон'), ('Хоккей'), ('Шахматы')
                        ''')
        connection.commit()

        # Создаём таблицу level_training
        cursor.execute('''
                    CREATE TABLE level_training(
                        id_level INTEGER PRIMARY KEY AUTOINCREMENT,
                        name varchar(255) NOT NULL)
                ''')
        connection.commit()
        # Заполнение таблицы
        cursor.execute('''
                    INSERT INTO level_training(
                        name)
                        VALUES
                        ('Начинающий'), ('Любитель'), ('Профессионал')
                        ''')
        connection.commit()

        # Создаём таблицу accaunt_type
        cursor.execute('''
                    CREATE TABLE accaunt_type(
                        id_type INTEGER PRIMARY KEY AUTOINCREMENT,
                        name varchar(255) NOT NULL)
                ''')
        connection.commit()
        # Заполнение таблицы
        cursor.execute('''
                    INSERT INTO accaunt_type(
                        name)
                        VALUES
                        ('Тренер'), ('Спортсмен'), ('Администратор')
                        ''')
        connection.commit()

        # Создаём таблицу place
        cursor.execute('''
                            CREATE TABLE place(
                                id_place INTEGER PRIMARY KEY AUTOINCREMENT,
                                name varchar(255) NOT NULL)
                        ''')
        connection.commit()
        # Заполнение таблицы
        cursor.execute('''
                            INSERT INTO place(
                                name)
                                VALUES
                                ('Спортивный клуб/зал'), ('Улица'), ('Онлайн'), ('В любом месте')
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