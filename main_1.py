from __future__ import annotations


#Задача №1.
# Сформировать класс "Animal" для представления сущности «Животное» в программе. В качестве полей задаются:
# имя животного (строка), вид животного(строка), возраст (число). Реализовать следующие операции:
# вывести звук, который издает животное (строка). Реализовать метод вывода информации оживотном на экран.
# Метод вывода на экран должен аккумулировать состояние полей объекта.

class Animal:

    name: str
    animal_species: str
    age: float

    def __init__(self, name: str, animal_species: str, age: float):

        self.name = name
        self.animal_species = animal_species
        self.age = age

    def __str__(self):

        return f"Животное {self.name}, вид {self.animal_species}. Возраст {self.age} годика-ов."

    def get_sound(self):

        if self.animal_species.lower() == "корова":
            return "му-уу. Проще говоря -мычит"

        elif self.animal_species.lower() == "лошадь":
            return "иго-го. Проще говоря -ржет"

        elif self.animal_species.lower() == "собака":
            return "гав-гав. Проще говоря -лает"

        elif self.animal_species.lower() == "баран":
            return "бе-еее. Проще говоря -блеет"

        else:
            return f"нечленораздельный звук!"

    def make_sound(self):
        sound = self.get_sound()
        return f"издает звук: {sound}"

    def sound_pls(self):
        return f"{self.animal_species} издай звук-"

a = Animal("Мурзик", "козел", 5)
p = Animal.sound_pls(a)
m = Animal.make_sound(a)


# Задача №2.
# Сформировать класс «Book» для представления сущности «Книга» в программе.
# В качестве полей задаются: наименование книги (строка), автор книги (строка), количество страниц (число).
# Реализовать операции: «отрыть» указанную страницу (на вход в метод передается номер страницы и выводится строка,
# открылась страница или нет). Реализовать метод вывода информации о книге на экран.
# Метод вывода на экран должен аккумулировать состояние полей объекта.

class Book:
    title: str
    autor: str
    num_pages: int
    def __init__(self, title: str, autor: str, num_pages: int):

        if not num_pages > 0:
            raise ValueError("Страниц в книге не может быть равно или меньше нуля")

        self.title = title
        self.autor = autor
        self.num_pages = num_pages

    def open_pages(self):
        n = int(input("Введите номер страницы > "))

        if not n <= self.num_pages:
            raise ValueError(f"Номер введенной Вами страницы {n}, превышает количество страниц книги в {self.num_pages} стр.")

        return f"{n} странице"

    def __str__(self):
        return f"Книга: название -\"{self.title}\". Автор -\"{self.autor}\". Объемом {self.num_pages} стр.\nОткрыта читателем на {self.open_pages()}"


b = Book("Паспорт", "Маяковский", 12)


# Задача №3.
# Сформировать класс «PassengerPlane» для представления сущности «Пассажирский Самолет» в программе.
# В качестве полей задаются:
# производитель самолета, модель самолета, вместимость пассажиров, текущая высота, текущая скорость.
# Реализовать следующие операции: взлет самолета, посадка самолета, изменение высоты, изменение скорости.
# Реализовать метод вывода информации о пассажирском самолете на экран. Метод вывода на экран должен
# аккумулировать состояние полей объекта.
# Примечание:
# Взлет самолета – операция, которая выводит сообщение на консоль «Самолет взлетел!».
# Посадка самолета – операция, которая выводит сообщение на консоль «Самолет приземлился!».
# Изменение высоты – операция, которая на вход принимает новое значение высоты и заменяет старое.

class PassengerPlane:

    constructor: str
    model: str
    capacity: int
    current_altitude: float
    current_speed: float
    def __init__(self, constructor: str, model: str, capacity: int, current_altitude=0.0, current_speed=0.0):

        self.constructor = constructor
        self.model = model
        self.capacity = capacity
        self.current_altitude = float(current_altitude)
        self.current_speed = float(current_speed)

    def __str__(self):
        return f"""Самолет {self.constructor}{self.model}, подготовлен к взлету. Пассажиров: {self.capacity} чел. + 8 чел. экипажа.
Текущее состояние: текущая скорость {self.current_speed} км/ч; текущая высота {self.current_altitude} м. над уровнем моря."""

    def __add__(self, other):
        new_speed = self.current_speed + other
        new_altitude = self.current_altitude + other

        return PassengerPlane(self.constructor, self.model, self.capacity, new_altitude, new_speed)

    def __sub__(self, other):
        new_speed = self.current_speed - other
        new_altitude = self.current_altitude - other

        return PassengerPlane(self.constructor, self.model, self.capacity, new_altitude, new_speed)

    def running_start(self): # метод взлета

        speed_increase = 300.0
        altitude_increase = 10.0
        print(f"Начинаем разгон самолета {self.constructor}{self.model} на {speed_increase} км/ч..")

        self.current_speed += speed_increase
        self.current_altitude += altitude_increase

        return (f"""Самолет {self.constructor}{self.model} разгоняется для взлета, текущая скорость = {self.current_speed} км/ч.
Произошел отрыв от земли, текущая высота {self.current_altitude} м. Самолет взлетел.""")

    def change_height(self): # метод изменения высоты

        self.current_altitude = 10500.0
        self.speed_increase = 1350.0

        print(f"Самолет летит. Текущая высота полета {self.current_altitude} м, текущая скорость {self.speed_increase} км/ч")

        reduction_altitude = float(input("Введите желаемый параметр снижения высоты > "))

        if reduction_altitude < self.current_altitude:

            self.current_altitude -= reduction_altitude
            print(f"Произошло снижение высоты на {reduction_altitude}. Текущая высота полета {self.current_altitude} м")

        else:
            raise ValueError("Снижение высоты не может превышать текущую. Иначе ... кабздец!")

        surge_altitude = float(input("Введите желаемый параметр увеличения высоты > "))

        self.current_altitude += surge_altitude

        return f"Произошло увеличение высоты полета на {surge_altitude} м. Текущая высота полета {self.current_altitude} м"


l = PassengerPlane("Ту-", "154", 120)
print(l)
r = l.running_start()
print(r)
c = l.change_height()
print(c)
ch = l.change_height()
print(ch)