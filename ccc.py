import random

class Book: #родительский класс с данными 
    def __init__(self):
        self.books_dict = {
            "Энциклопедия": [8, 10, 6],
            "Приключения": [17, 2, 18],
            "Словарь": [9, 6, 1],
            "Учебник": [10, 1, 7],
            "Фантастика": [20, 8, 4],
            "Комикс": [5, 6, 9]
        }

class Deliver(Book): #наследственный класс курьера
    deliver_dict = {"Шарипов Резван": 50903}
    salary = 0 #переменная для подсчета зарплаты
    counter = 0 #переменная для подсчета выполненной работы курьера

    def __init__(self, deliver_name: str, code: int): #инициализация
        self.deliver_name = deliver_name
        self.code = code
        super().__init__()

    def entry_dict(self): #проверка пользователя в системе
        return self.deliver_name in Deliver.deliver_dict

    def dev_varification(self): #верификация
        if self.deliver_name in Deliver.deliver_dict and self.code == Deliver.deliver_dict[self.deliver_name]:
            print("Верификация прошла успешно")
            return True
        else:
            raise ValueError("Проверьте точно ли это код доставщика")

    def registration(self, data: str): #регистрация
        if self.entry_dict():
            print("Вы уже зарегистрированы.")
            return True
        if len(data.split('.')) == 3 and all(d.isdigit() for d in data.split('.')):
            self.data = data
            self.code = random.randint(10000, 99999)
            Deliver.deliver_dict[self.deliver_name] = self.code 
            print(f"Ваш код доставщика {self.code}")
            return True
        else:
            print("Неверный формат даты")
            return False

    def deliv(self): #функция для основного процесса работы
        if not self.entry_dict():
            print("Не найден курьер")
            return False
        if not self.dev_varification():
            return False
        print("Введите книги и их количество которые вы завозите (например, 'Комикс,2'):")
        while True:
            entry = input()
            if entry.lower() == "ничего":
                print("Зачем тогда приехал")
                break
            try:
                book, quantity = entry.split(',')
                book = book.strip().title()
                quantity = int(quantity.strip())
                if quantity <= 0:
                    print("Невозможно завести отрицательное количество книг или 0")
                    continue
                if book in self.books_dict:
                    self.books_dict[book][0] += quantity
                    Deliver.salary += 1000 * quantity 
                    Deliver.counter += quantity 
                    print(f"Курьер {self.deliver_name}, завез в библиотеку книгу {book} в указанном количестве {quantity}")
                else:
                    self.books_dict[book] = [quantity, None, None]  
                    print(f"Курьер {self.deliver_name}, завез в библиотеку новую книгу {book} в указанном количестве {quantity}")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите название книги и количество через запятую.")



class DeliverInfo(Deliver): #класс для подсчета данных и выдачи зарплаты
    info_deliver_dict = {
        "Имя доставщика": None, 
        "Отдано книг": None,
        "Получено денег": None
    }

    def __init__(self):
        super().__init__("Имя не задано", 0)  

    def deliver_salary(self):
        DeliverInfo.info_deliver_dict["Имя доставщика"] = self.deliver_name  
        DeliverInfo.info_deliver_dict["Отдано книг"] = Deliver.counter
        DeliverInfo.info_deliver_dict["Получено денег"] = Deliver.salary
        return True


