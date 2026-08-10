class Animal:
    def eat(self):
        print("Животное кушает")

    def sleep(self):
        print("Животное спит")

    def speak(self):
        raise NotImplementedError("Метод speak() должен быть переопределён")


class Dog(Animal):
    def speak(self):
        print("Гав Гав")


class Cat(Animal):
    def speak(self):
        print("Мяу")


class Lion(Animal):
    def speak(self):
        print("Ррр")


class Elephant(Animal):
    def speak(self):
        print("Труууу")


def zoo_show(animals):
    for animal in animals:
        animal.eat()
        animal.sleep()
        animal.speak()
        print()


animals = [
    Dog(),
    Cat(),
    Lion(),
    Elephant()
]

zoo_show(animals)