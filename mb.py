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

class Reader(Book): #наследственный класс для пользователя
    info_dict = {} #данные для последующего подсчета 
    debt_dict = {} #данные для последующего подсчета 
    counter1 = 0 #данные для последующего подсчета
    counter2 = 0 #данные для последующего подсчета
    
    def __init__(self, name: str, numb: int = None, phone_number: str = None): #инициализация
        super().__init__()
        self.name = name
        self.numb = numb
        self.phone_number = phone_number
        self.data = None
    
    def entry_array(self): #проверка на нахождение пользователя в системе
        return self.name in Reader.info_dict
    
    def registration(self, data: str): #регистрация
        if self.entry_array():
            print("Вы уже зарегистрированы.")
            return True
        if len(data.split('.')) == 3 and all(d.isdigit() for d in data.split('.')):
            self.data = data
            self.numb = random.randint(1000, 9999)
            Reader.info_dict[self.name] = [self.phone_number, self.numb]
            print(f"Ваш номер билета {self.numb}")
            return True
        else:
            print("Неверный формат даты")
            return False
    
    def numb_checker(self): #проверка читательского билета
        if self.numb and self.numb == Reader.info_dict.get(self.name)[1] and len(str(self.numb)) == 4:
            print("Номер подтвержден.")
            return True
        else:
            print("Проверьте точно ли это ваш номер")
            return False
    
    def phone_number_check(self): #проверка номера телефона
        if self.phone_number and len(self.phone_number) == 12 and self.phone_number.startswith('+7') and self.phone_number == Reader.info_dict.get(self.name)[0]:
            print("Номер телефона подтвержден.")
            return True
        else:
            raise ValueError("Проверьте точно ли это ваш номер телефона")
    
    def search(self): #поиск товара
        if not self.entry_array():
            print("Пользователь не зарегистрирован.")
            return
        print("Что вы хотите найти?")
        while True:
            entry = input()
            if entry.lower() == 'выход':
                break
            book = entry.strip().title()
            if book in self.books_dict:
                print(f"Количество книг '{book}': {self.books_dict[book][0]}") 
            else:
                print("Книги нет в наличии")
    
    def takebook(self): #процесс взятия книг из библиотеки
        if not self.entry_array():
            print("Пользователь не зарегистрирован.")
            return
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
                    self.books_dict[book][0] -= quantity  
                    Reader.debt_dict[self.name] = [book, quantity]  
                    print(f'{self.name}, взял {quantity} книг(и) "{book}". В случае потери звонить по номеру {self.phone_number}')
                    Reader.counter1 += quantity 
                else:
                    print(f"Книги \"{book}\" нет в наличии или она не существует.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите название книги и количество через запятую.")
    
    def returnbook(self): #процесс возвращения книг в библиотеку
        if not self.entry_array():
            print("Пользователь не зарегистрирован.")
            return
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
                    print("Невозможно вернуть отрицательное количество книг или 0")
                    continue
                if book in self.books_dict:
                    self.books_dict[book][0] += quantity 
                    if self.name in Reader.debt_dict and book in Reader.debt_dict[self.name]:
                        Reader.debt_dict[self.name].remove(book) 
                    print(f"Книга \"{book}\" в количестве {quantity} штук возвращена в библиотеку пользователем {self.name}")
                    Reader.counter2 += quantity 
                else:
                    print(f"Книги \"{book}\" нет в нашей системе.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите название книги и количество через запятую.")

rd = None
array = []
try: #верификация
    print("Добро пожаловать\nВерификация,Регистрация")
    a = str(input())
    if a.lower() == "верификация":
        name: str = input("Введите имя: ")
        numb = int(input("Введите номер читательского билета: "))
        phone_number = input("Введите номер телефона: ")
        rd = Reader(name, numb, phone_number)
        if rd.entry_array():
            if rd in array:
                rd.numb_checker()
                rd.phone_number_check()
        else:
            print("Пользователь не найден.")
    elif a.lower() == "регистрация":
        name: str = input("Введите имя: ")
        phone_number = input("Введите номер телефона: ")
        data = str(input("Введите вашу дату:"))
        rd = Reader(name, None, phone_number)
        if rd.registration(data):
            rd.phone_number_check()
            array.append(rd)
    else:
        print("Вы не зарегистрированы. Пожалуйста, зарегистрируйтесь.")
        name: str = input("Введите имя: ")
        phone_number = input("Введите номер телефона: ")
        data: str = input("Введите дату: ")
        rd = Reader(name, None, phone_number)
        if not rd.registration(data):
            raise ValueError("Ошибка регистрации")
        else:
            array.append(rd)

    while True: #основной процесс
        if rd:
            action = input("Что вы хотите сделать (взять/вернуть/найти/выйти): ").lower()
            if action == "взять":
                rd.takebook()
            elif action == "вернуть":
                rd.returnbook()
            elif action == "выйти":
                print("Возвращайтесь снова")
                break
            elif action == "найти":
                rd.search()
            else:
                print("Такого варианта нету")
        else:
            print("Ошибка: объект читателя не был создан.")
            break
except KeyboardInterrupt:
    print("\nПрограмма была прервана пользователем")
except Exception as e:
    print("Произошла ошибка:", e)




class Info(Book): #класс для последующей отчетности за день
    info_dict = {
        "Остаток": None,
        "Взяли": None,
        "Вернули": None
    }

    def __init__(self):
        super().__init__()

    def ostatok(self):
        total = 0
        for key in self.books_dict:
            total += self.books_dict[key][0]
        Info.info_dict["Остаток"] = total
        return Info.info_dict["Остаток"]
    
    def take(self):
        Info.info_dict["Взяли"] = Reader.counter1
        return Info.info_dict["Взяли"]
    
    def refund(self):
        Info.info_dict["Вернули"] = Reader.counter2
        return Info.info_dict["Вернули"]
    
    


        


