from abc import ABC, abstractmethod

class Character(ABC):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        if 0 <= value <= 100:
            self.__health = value
        else:
            raise ValueError("Здоровье должно быть от 0 до 100.")

    @abstractmethod
    def attack(self):
        pass

    def take_damage(self, damage):
        self.health = max(0, self.health - damage)


class Warrior(Character):
    def __init__(self, name, health, weapon):
        super().__init__(name, health)
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} атакует с помощью {self.weapon}!")


class Mage(Character):
    def __init__(self, name, health, spell):
        super().__init__(name, health)
        self.spell = spell

    def attack(self):
        print(f"{self.name} использует заклинание {self.spell}!")

warrior = Warrior("Диас", 100, "меч")
mage = Mage("Мерлин", 80, "Огненный шар")

characters = [warrior, mage]
for character in characters:
    character.attack()

