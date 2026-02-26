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
        return f"Издает звук: {sound}"

    def sound_pls(self):
        return f"{self.animal_species} издай звук"

a = Animal("Тузик", "Собака", 5)
p = Animal.sound_pls(a)
m = Animal.make_sound(a)
print(a, p, m)
