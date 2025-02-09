import os

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