class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        return f"Обитатель зоопарка {self.name} умеет издавать звуки"

    def eat(self):
        return f"Обитатель зоопарка {self.name} любит покушать"

    def get_name(self):
        return self.name


class Bird(Animal):
    def __init__(self, Genus, feathers):
        name = input("Введите имя птицы: ")
        age = int(input("Введите возраст птицы: "))
        super().__init__(name, age)
        self.Class = 'Aves'
        self.temper = 'warm-blooded'
        self.Genus = Genus
        self.feathers = feathers

    def make_sound(self):
        return f"Птичка по имени {Animal.get_name(self)} принадлежит роду '{self.Genus}' и умеет петь"


class Mammal(Animal):
    def __init__(self, Genus, fur):
        name = input("Введите имя млекопитающего: ")
        age = int(input("Введите возраст млекопитающего: "))
        super().__init__(name, age)
        self.Class = 'Mammalia'
        self.temper = 'warm-blooded'
        self.Genus = Genus
        self.fur = fur

    def make_sound(self):
        return f"Млекопитающее по имени {Animal.get_name(self)} принадлежит роду '{self.Genus}' и имеет голос"


class Reptile(Animal):
    def __init__(self, Genus, skin):
        name = input("Введите имя рептилии: ")
        age = int(input("Введите возраст рептилии: "))
        super().__init__(name, age)
        self.Class = 'Reptilia'
        self.temper = 'cold-blooded'
        self.Genus = Genus
        self.skin = skin

    def make_sound(self):
        return f"Рептилия по имени {Animal.get_name(self)} принадлежит роду '{self.Genus}' и не имеет голоса"

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())


animals = [Bird('Соловей', 'Серый'),
           Mammal('Лошадь', 'Каурая'),
           Reptile('Гадюка', 'Черная')]
animal_sound(animals)

