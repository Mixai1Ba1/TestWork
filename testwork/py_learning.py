# структуру данных
# классы
# ооп
# синтаксис
# функции
# (декораторы)
# замыкание

# структуру данных
# Списки (Lists):
# Это упорядоченные коллекции элементов, которые могут быть изменены.
# Элементы списка можно изменять, добавлять, удалять.
number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
result = number[0] + number[8]
print(number[0], number[8], "=", result)
# К элементам списка можно обращаться по индексу, например: numbers[0] вернёт 1.

# Кортежи (Tuples):
# 	Это также упорядоченные коллекции элементов, но они неизменяемы.
# 	После создания кортежа его элементы нельзя изменять.
cord = (10, 20)
print(cord[0], cord[1])

# Множества (Sets):
# 	Это неупорядоченные коллекции уникальных элементов.
# 	В множестве не может быть повторяющихся элементов.
uniq_num = {
    2,
    2,
    2,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    12,
    13,
    14,
}
uniq_list = list(uniq_num)
print(uniq_list[0], uniq_list[1], uniq_num)

uniq_num = {1, 2, 3, 4, 5, 6, 7}
for num in uniq_num:
    print(num)

# Словари (Dictionaries):
# 	Это неупорядоченные коллекции пар “ключ-значение”.
# 	Ключи должны быть уникальными, а значения могут быть любыми.

# student = {'name': 'Shamil', 'age': 200, 'major': 'Computer Science'}
student = [
    {"name": "Shamil", "age": 200, "major": "Computer Science"},
    {"name": "albert", "age": 10, "major": "shool of Engineering"},
]
# student['name'] = 'John'
for stud in student:
    print(stud["name"], stud["age"], stud["major"])

# Классы -это способ создания пользовательских типов данных.
# Классы позволяют объединить данные и методы (функции),
# которые работают с этими данными, в одну структуру.

# Создание класса:
# 	Класс объявляется с помощью ключевого слова class.
# 	Внутри класса можно определить атрибуты (данные) и методы (функции).


class x:
    def __init__(self, name, age, surname):
        self.name = name
        self.surname = surname
        self.age = age

    # Метод __init__:
    # Это специальный метод-конструктор, который вызывается при создании объекта. Он используется для инициализации атрибутов объекта.

    def im(self):
        return (
            f"Hello, my name is {self.name} {self.surname}. I am {self.age} years old."
        )


# Создание экземпляра класса:
first_x = x("Хуес", 220, "Ос")  # экземлпяр клааса x
print(first_x.im())


# наследование
class childofxeysos(x):
    def speak(self):
        return (
            f"Hello, my name is {self.name} {self.surname}. I am {self.age} years old."
        )


print(first_x.im())


# абстракция
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__engine_started = False  # приватный атрибут два подчеркивания

    def start_engine(self):
        self.__engine_started = True
        print("engine started")

    def stop_engine(self):
        self.__engine_started = False
        print("eng stopped")

    def drive(self):
        if self.__engine_started:
            print(f"the {self.make} {self.model} is driving")
        else:
            print("you need to start the engine first")


my_car = Car("toyota", "camry", 2022)
my_car.start_engine()
my_car.drive()
my_car.stop_engine()


# полиморфизм
# позволяет методам в подклассах переопределять методы из родительских классов
# позволяет одному интерфейсу обрабатывать объекты разных типов
class animal:
    def speak(self):
        raise NotImplementedError("subclass must implement abstract method")
# специальный тип исключения в Python, который указывает, что метод или функция не были реализованы. Если вы пытаетесь вызвать такой метод без его реализации, NotImplementedError будет вызван, сигнализируя о том, что метод должен быть реализован в дочерних классах
class dog(animal):
    def speak(self):
        return "Woof!"


class cat(animal):
    def speak(self):
        return "Meow!"


def animal_speak(animal):
    print(animal.speak())

def animal_speak(animal):
    try:
        print(animal.speak())
    except NotImplementedError as e:
        print(e)

#объекты
dog = dog()
cat = cat()
animal = animal()

animal_speak(dog)  
animal_speak(cat)  
animal_speak(animal)  


#инкапсуляция- это принцип, который скрывает детали реализации и предоставляет доступ 
# только к тому, что необходимо. 
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner        #публичное свойство 
        self._balance = balance   #защищённый атрибут (доступен для изменения только в пределах класса и подклассов)
        self.__pin = 1234         #приватный атрибут (доступен только внутри класса)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited {amount}. New balance: {self._balance}")

    def minus(self, amount, pin):
        if pin == self.__pin:
            if amount > 0 and amount <= self._balance:
                self._balance -= amount
                print(f"Minus {amount}. New balance: {self._balance}")
            else:
                print("Insufficient funds or invalid amount.")
        else:
            print("Invalid PIN.")

account = BankAccount("John Doe", 1000)
print(account.owner)
#доступ к защищённому атрибуту (возможно, но не рекомендуется)
print(account._balance) 

#к приватному атрибуту вызовет ошибку
#print(account.__pin)  #AttributeError

# Использование методов для доступа и изменения данных
account.deposit(500)        # Выведет: Deposited 500. New balance: 1500
account.minus(200, 1234) # Выведет: Minus 200. New balance: 1300


