from abc import ABC, abstractmethod
import random
import time


class Gladiator(ABC):
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    @abstractmethod
    def attack(self, opponent):
        pass

    @abstractmethod
    def take_damage(self, damage):
        pass

    def is_alive(self):
        return self.health > 0


class Maximus(Gladiator):
    def __init__(self):
        super().__init__('Максимус', 100, 25)

    def attack(self, opponent):
        print(f"{self.name} бьёт {opponent.name}а с силой {self.attack_power}")
        opponent.take_damage(self.attack_power)
        self.attack_power -= 1

    def take_damage(self, damage):
        self.health -= damage
        print(f"У {self.name}а осталось жизни {self.health}")
        if self.health <= 0:
            print(f"Он погибает :(")


class Spartacus(Gladiator):
    def __init__(self):
        super().__init__('Спартак', 101, 24)

    def attack(self, opponent):
        print(f"{self.name} бьёт {opponent.name}а с силой {self.attack_power}")
        opponent.take_damage(self.attack_power)
        self.attack_power -= 1

    def take_damage(self, damage):
        self.health -= damage
        print(f"У {self.name}а осталось жизни {self.health}")
        if self.health <= 0:
            print(f"Он погибает :(")


class Crixus(Gladiator):
    def __init__(self):
        super().__init__('Крикс', 99, 26)

    def attack(self, opponent):
        print(f"{self.name} бьёт {opponent.name}а с силой {self.attack_power}")
        opponent.take_damage(self.attack_power)
        self.attack_power -= 1

    def take_damage(self, damage):
        self.health -= damage
        print(f"У {self.name}а осталось жизни {self.health}")
        if self.health <= 0:
            print(f"Он погибает :(")

class Commodus(Gladiator):
    def __init__(self):
        super().__init__('Коммод', 98, 27)

    def attack(self, opponent):
        print(f"{self.name} бьёт {opponent.name}а с силой {self.attack_power}")
        opponent.take_damage(self.attack_power)
        self.attack_power -= 2

    def take_damage(self, damage):
        self.health -= damage
        print(f"У {self.name}а осталось жизни {self.health}")
        if self.health <= 0:
            print(f"Он погибает :(")


class Draw:
    @staticmethod
    def get_random_opponents():
        glad1, glad2 = random.sample([Maximus(), Spartacus(), Crixus(), Commodus()], 2)
        user_choice = int(input(f"Жребий выбрал гладиаторов для боя:\n"
                            f"1 - {glad1.name}, запас жизни {glad1.health}, сила удара {glad1.attack_power} \n"
                            f"2 - {glad2.name}, запас жизни {glad2.health}, сила удара {glad2.attack_power} \n"
                            f"Выберите номер своего бойца:  "))
        if user_choice == 1:
            return glad1, glad2
        elif user_choice == 2:
            return glad2, glad1
        else:
            print("Нужно ввести 1 или 2")
            return Draw.get_random_opponents()


def rock_paper_scissors():
    comp_win, user_win = 0, 0
    choices = ['камень', 'ножницы', 'бумага']
    outcome = {
        ('камень', 'ножницы'): True,
        ('ножницы', 'бумага'): True,
        ('бумага', 'камень'): True
    }
    while comp_win == 0 and user_win == 0:
        comp_choice = random.choice(choices)
        user_choice = input("Выберите: камень, ножницы или бумага: ").lower()
        if user_choice not in choices:
            print("Неправильный выбор. Пожалуйста, введите одно из трех слов.")
            continue
        print(f"Компьютер выбрал: {comp_choice}")

        if user_choice == comp_choice:
            print("Ничья. Еще раз:")
        elif outcome.get((comp_choice, user_choice), False):
            comp_win += 1
            print(f"Вы проиграли право на первый удар.")
        else:
            user_win += 1
            print(f"Вы выиграли право на первый удар.")
    return user_win


class Battle:
    @staticmethod
    def start():
        user_glad, comp_glad = Draw.get_random_opponents()
        print("Разыграем право первого удара.")
        if rock_paper_scissors() == 1:
            glad1, glad2 = user_glad, comp_glad
        else:
            glad1, glad2 = comp_glad, user_glad
        time.sleep(3)
        print("Кровавая бойня начинается!!!")
        time.sleep(3)
        while glad1.is_alive() and glad2.is_alive():
            glad1.attack(glad2)
            time.sleep(3)
            if glad2.is_alive():
                glad2.attack(glad1)
                time.sleep(3)
            luck = random.randint(0, 2)
            if luck <= 1:
                if glad1.health > glad2.health:
                    lucky = glad2
                    unlucky = glad1
                else:
                    lucky = glad1
                    unlucky = glad2
                if unlucky.is_alive() and lucky.is_alive():
                    print(f"Внезапно {unlucky.name} пропускает удар")
                    lucky.attack(unlucky)
                    time.sleep(3)
        if glad1.is_alive():
            print(f"Победил {glad1.name}!")
        else:
            print(f"Победил {glad2.name}!")


if __name__ == '__main__':
    Battle.start()

