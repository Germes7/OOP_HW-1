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
    
    def get_sound(self):

        if self.animal_species.lower() == "корова":
            return "му-уу"

        elif self.animal_species.lower() == "лошадь":
            return "иго-го"

        elif self.animal_species.lower() == "собака":
            return "гав-гав"

        elif self.animal_species.lower() == "баран":
            return "бе-еее"

        else:
            return f"нечленораздельный звук"

    def make_sound(self):
        sound = self.get_sound()
        return f"Животное {self.animal_species}. Издает звук {sound}"

a = Animal("Буренка", "корова", 4.5)
s = Animal.make_sound(a)
print(a)
print(s)