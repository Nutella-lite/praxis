class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print(f"Обитатель зоопарка {self.name} умеет издавать звуки")

    def eat(self):
        print(f"Обитатель зоопарка {self.name} любит покушать")

    def get_name(self):
        return self.name


class Bird(Animal):
    def __init__(self):
        name = input("Введите вид птицы: ")
        age = int(input("Введите возраст птицы: "))
        super().__init__(name, age)
        self.Class = 'Aves'
        self.temper = 'warm-blooded'

    def make_sound(self):
        print(f"Обитатель зоопарка '{self.name}' принадлежит классу '{self.Class}' и умеет петь")


class Mammal(Animal):
    def __init__(self):
        name = input("Введите вид млекопитающего: ")
        age = int(input("Введите возраст млекопитающего: "))
        super().__init__(name, age)
        self.Class = 'Mammalia'
        self.temper = 'warm-blooded'

    def make_sound(self):
        print(f"Обитатель зоопарка '{self.name}' принадлежит классу '{self.Class}' и имеет голос")


class Reptile(Animal):
    def __init__(self):
        name = input("Введите вид рептилии: ")
        age = int(input("Введите возраст рептилии: "))
        super().__init__(name, age)
        self.Class = 'Reptilia'
        self.temper = 'cold-blooded'

    def make_sound(self):
        print(f"Обитатель зоопарка '{self.name}' принадлежит классу '{self.Class}' и не имеет голоса")


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()


class Zoo:
    def __init__(self):
        self.animals = []
        self.employees = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"Добавлено животное {animal.get_name()}")

    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Добавлен работник {employee}")


class ZooKeeper:
    def feed_animal(self, animal):
        print(f"Смотритель кормит животное '{animal.name}'")


class Veterinarian:
    def heal_animal(self, animal):
        print(f"Ветеринар лечит животное '{animal.name}'")


zoo = Zoo()
running = True
while running:
    action = int(input("Выберите действие: "
                       "\n1 - добавить животное "
                       "\n2 - добавить птицу "
                       "\n3 - добавить млекопитающее "
                       "\n4 - добавить рептилию "
                       "\n5 - добавить работника "
                       "\n6 - вывести весь зоопарк на экран "
                       "\n7 - выход из программы \n"))
    if action == 1:
        zoo.add_animal(Animal(input("Введите вид животного: "), int(input("Введите возраст животного: "))))
    elif action == 2:
        bird = Bird()
        zoo.add_animal(bird)
    elif action == 3:
        mammal = Mammal()
        zoo.add_animal(mammal)
    elif action == 4:
        reptile = Reptile()
        zoo.add_animal(reptile)
    elif action == 5:
        employee = input("Введите имя работника: ")
        zoo.add_employee(employee)
    elif action == 6:
        for animal in zoo.animals:
            print(f"{animal.get_name()} (класс - {animal.__class__.__name__}, возраст - {animal.age})")
        animal_sound(zoo.animals)
        for employee in zoo.employees:
            print(f"Работник: {employee}")
    else:
        running = False