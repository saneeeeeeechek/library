import random

class Book: #родительский класс с данными о книгах
    def __init__(self):
        self.books_dict = {
            "Энциклопедия": [8, 10, 6],
            "Приключения": [17, 2, 18],
            "Словарь": [9, 6, 1],
            "Учебник": [10, 1, 7],
            "Фантастика": [20, 8, 4],
            "Комикс": [5, 6, 9]
        }

class Salesman(Book): #наследственный класс для покупателя
    salesman_dict = {"Саночкин Ростислав": "sqlpyc++c#js"}
    salary = 0
    week = ["понедельник", "вторник", "среда", "четверг", "пятница", "суббота", "воскресенье"]
    counter = 0

    def __init__(self, salesman_name: str, password: str): #инициализация данных 
        self.salesman_name = salesman_name
        self.password = password
        super().__init__()

    def entry_dict(self): #функция для определения пользователя в системе
        return self.salesman_name in Salesman.salesman_dict

    def sales_varification(self):#определение пользователя
        if self.salesman_name in Salesman.salesman_dict and self.password == Salesman.salesman_dict[self.salesman_name]:
            print("Верификация прошла успешно")
            return True
        else:
            raise ValueError("Проверьте точно ли это пароль")

    def registration(self, data: str):#регистрация пользователя
        if self.entry_dict():
            print("Вы уже зарегистрированы.")
            return True
        if len(data.split('.')) == 3 and all(d.isdigit() for d in data.split('.')):
            self.data = data
            self.password = password  
            Salesman.salesman_dict[self.salesman_name] = self.password
            working_days = list(random.choice(Salesman.week) for i in range(3))  
            print(f"{self.salesman_name}, вы успешно зарегистрировались. Ваши рабочие дни: {', '.join(working_days)}")
            return True
        else:
            print("Неверный формат даты")
            return False
    
    def password(self):#функция похожая на шифрования данных,но она не доработанная
        if self.registration:
            hidden_password = '*' * len(self.password)
            Salesman.salesman_dict[self.salesman_name] = self.password
            return hidden_password  

    def sales(self):#функция для основной работы продавца
        if not self.entry_dict():
            print("Пользователь не продавец.")
            return False
        print("Введите название книги и количество через запятую (например, 'Энциклопедия, 2'):")
        while True:
            entry = input()
            if entry.lower() == 'выход':
                break
            try:
                book, quantity = entry.split(',')
                book = book.strip().title()
                quantity = int(quantity.strip())
                if quantity <= 0:
                    print("Невозможно взять отрицательное количество книг или 0")
                    continue
                if book in self.books_dict and self.books_dict[book][0] >= quantity:
                    print(f"Книга {book} хранится в шкафу {self.books_dict[book][1]} на полке {self.books_dict[book][2]}")
                    Salesman.salary += 1000 * quantity
                    Salesman.counter += 1
                else:
                    print(f"Книги \"{book}\" нет в наличии или она не существует.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите название книги и количество через запятую.")

        

sl = None
array = []
try: #система верификации
    print("Добро пожаловать\nВерификация,Регистрация") 
    a = str(input()) 
    if a.lower() == "верификация":
        name = str(input("Введите свое имя: "))
        password = str(input("Введите свой пароль: "))
        sl = Salesman(name, password)
        if sl.entry_dict() and sl.sales_varification():
            if sl in array:
                print("Верификация успешна.")
        else:
            print("Верификация не удалась.")
    elif a.lower() == "регистрация": 
        name = str(input("Введите имя: "))
        password = str(input("Придумайте пароль: "))
        data = str(input("Введите вашу дату:")) 
        sl = Salesman(name, password)
        array.append(sl)
        if sl.registration(data):
            print("Регистрация успешна.")
            sl.password()
        else:
            print("Ошибка регистрации.")
    else:
        print("Вы не зарегистрированы. Пожалуйста, зарегистрируйтесь.") 
        name = str(input("Введите имя: "))
        password = str(input("Придумайте пароль: "))
        data = str(input("Введите вашу дату:")) 
        sl = Salesman(name, password)
        if not sl.registration(data):
            raise ValueError("Ошибка регистрации")
        else:
            array.append(sl)    
            sl.password() 

    while True: #процесс работы
        if sl:
            a = str(input("Начало дня. Подтвердитесь (+). При уходе нажмите (-): "))
            if a == "+":
                sl.sales()
            elif a == "-":
                print("Хорошего дня или вечера!")
                sl.info()
                break
            else:
                print("Неверный ввод. Пожалуйста, используйте '+' для начала работы или '-' для завершения.")
        else: 
            print("Ошибка: объект продавца не был создан.") 
            break 
except KeyboardInterrupt:
    print("\nПрограмма была прервана пользователем")
except Exception as e:
    print("Произошла ошибка:", e)

class InfoSalesman(Book): #класс для показания отчетности продавца
    info_salesman_dict = {
        "Выполненная работа": None,
        "Зарплата": None
    }
    
    def __init__(self):
        super().__init__()

    def salary(self):
        InfoSalesman.info_salesman_dict["Выполненная работа"] = Salesman.counter
        InfoSalesman.info_salesman_dict["Зарплата"] = Salesman.salary
        return True




