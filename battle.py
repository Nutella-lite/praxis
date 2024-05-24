from abc import ABC, abstractmethod
import random


class Weapon(ABC):
    @abstractmethod
    def attack(self):
        pass

    @abstractmethod
    def is_effective_against_monster(self):
        pass


class Sword(Weapon):
    def __init__(self):
        self.name = 'меч'

    def attack(self):
        print(f"Боец атакует, используя {self.name}")

    def is_effective_against_monster(self):
        return True


class Bow(Weapon):
    def __init__(self):
        self.name = 'лук'

    def attack(self):
        print(f"Боец атакует, используя {self.name}")

    def is_effective_against_monster(self):
        return False


class Fist(Weapon):
    def __init__(self):
        self.name = 'кулаки'

    def attack(self):
        print(f"Боец атакует, используя {self.name}")

    def is_effective_against_monster(self):
        return False


class WeaponFactory:
    @staticmethod
    def get_random_weapon():
        return random.choice([Sword(), Bow(), Fist()])


class Fighter:
    def __init__(self):
        self.weapon = None

    def change_weapon(self):
        self.weapon = WeaponFactory.get_random_weapon()
        print(f"Боец выбирает {self.weapon.name}")

    def attack(self):
        self.weapon.attack()


class Monster:
    def __init__(self):
        self.win = True

    def repel(self, weapon):
        if weapon.is_effective_against_monster():
            print("Монстр побежден!")
            self.win = False
        else:
            print("Монстр побеждает... :(")


print("Бой начинается!")
fighter = Fighter()
while True:
    fighter.change_weapon()
    fighter.attack()

    monster = Monster()
    monster.repel(fighter.weapon)

    if not monster.win:
        break