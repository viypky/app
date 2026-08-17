#Принципы ООП: инкапсуляция и абстракция
# публичный self.balance
# защищенный self._balance
# приватный self.__balance

# class Bank:
#     def __init__(self, balance):
#         self.__balance = balance

#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#         else:
#             print("Значение должно быть больше 0")

#     def get_balance(self):
#         return self.__balance

# bank = Bank(1000)
# bank.deposit(10000)

# print(bank.get_balance()

# class Computer:
#     def __init__(self, brand, price, password):
#         self.brand = brand
#         self._price = price
#         self.__password = password

#     def get_password(self):
#         return self.__password

# computer = Computer("Hp", 80000, "1234")
# print(computer.brand)
# print(computer._price)
# print(computer.get_password())

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price

# @property #getter - для того чтобы получить
# def price(self):
#     return self._price

# @price.setter #setter - для того чтобы изменить
# def price(self, new_price):
#     if new_price > 0:
#         self._price = new_price
#     else:
#         print("Цена не должно быть меньше 0")

# product = Product("Телефон", 50000)

# print(product.name)
# print(product.price)

# product.price = 70000
# print(product.name)

# from abc import ABC, abstractclassmethod

# class Payment(ABC):
#     @abstractclassmethod
#     def pay(self, amount):
#         pass

# class CardPayment(Payment):

#     def pay(self, amount):
#         print(f"Оплата по картой {amount}")

# class CashPayment(Payment):

#     def pay(self, amount):
#         print(f"Оплата наличными {amount}")

# card = CardPayment()
# cash = CashPayment()

# card.pay(100)
# cash.pay(50)


from abc import ABC, abstractclassmethod
class Character(ABC):
    def __init__(self, name: str, health: int):
        self.name = name
        self.__health = 0 
        self.health = health

@property
def health(self) -> int:
    return self.__
