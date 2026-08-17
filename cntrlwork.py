# 1.
# class Product:
#     def __init__(self, name, price, quantity, category):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.category = category

#     def show_info(self):
#         print("Название:", self.name)
#         print("Цена:", self.price)
#         print("Количество:", self.quantity)
#         print("Категория:", self.category)

#     def change_price(self, new_price):
#         self.price = new_price

#     def add_quantity(self, amount):
#         self.quantity += amount

#     def remove_quantity(self, amount):
#         if amount <= self.quantity:
#             self.quantity -= amount

#     def check_product(self):
#         if self.quantity > 0:
#             return True
#         return False


# class User:
#     def __init__(self, name, email, balance):
#         self.name = name
#         self.email = email
#         self.balance = balance

#     def add_balance(self, amount):
#         self.balance += amount

#     def show_info(self):
#         print("Имя:", self.name)
#         print("Email:", self.email)
#         print("Баланс:", self.balance)


# class Order:
#     def __init__(self, user):
#         self.user = user
#         self.products = []
#         self.status = "Новый"

#     def add_product(self, product):
#         if product.quantity > 0:
#             self.products.append(product)
#             print(product.name, "добавлен в заказ")
#         else:
#             print(product.name, "нет в наличии")

#     def remove_product(self, product):
#         if product in self.products:
#             self.products.remove(product)

#     def get_total(self):
#         total = 0

#         for product in self.products:
#             total += product.price

#         return total

#     def change_status(self, status):
#         self.status = status

#     def show_info(self):
#         print("Пользователь:", self.user.name)
#         print("Статус заказа:", self.status)

#         for product in self.products:
#             print(product.name, "-", product.price)

#         print("Общая стоимость:", self.get_total())

#     def checkout(self):
#         total = self.get_total()

#         if self.user.balance >= total:
#             self.user.balance -= total

#             for product in self.products:
#                 product.quantity -= 1

#             self.status = "Оплачен"
#             print("Заказ оформлен")
#         else:
#             print("Недостаточно денег")


# product1 = Product("Телефон", 50000, 5, "Электроника")
# product2 = Product("Чехол", 1000, 10, "Аксессуары")
# product3 = Product("Наушники", 3000, 7, "Аксессуары")

# user = User("Анжелика", "viypkii@mail.com", 80000)

# order = Order(user)

# order.add_product(product1)
# order.add_product(product2)
# order.add_product(product3)

# print("Стоимость заказа:", order.get_total())

# order.checkout()

# print()
# order.show_info()

# print()
# user.show_info()

# 2.
# class Product:
#     def __init__(self, name, price, quantity, category):
#         self.name = name
#         self.price = price
#         self.quantity = quantity
#         self.category = category

#     def info(self):
#         print("Название:", self.name)
#         print("Цена:", self.price)
#         print("Количество:", self.quantity)
#         print("Категория:", self.category)

#     def change_price(self, new_price):
#         self.price = new_price

#     def add_quantity(self, amount):
#         self.quantity += amount

#     def remove_quantity(self, amount):
#         if amount <= self.quantity:
#             self.quantity -= amount


# class Electronics(Product):
#     def __init__(self, name, price, quantity, category, warranty, manufacturer):
#         super().__init__(name, price, quantity, category)
#         self.warranty = warranty
#         self.manufacturer = manufacturer

#     def info(self):
#         print("Название:", self.name)
#         print("Цена:", self.price)
#         print("Количество:", self.quantity)
#         print("Категория:", self.category)
#         print("Производитель:", self.manufacturer)
#         print("Гарантия:", self.warranty, "месяцев")


# class Clothes(Product):
#     def __init__(self, name, price, quantity, category, size, material, color):
#         super().__init__(name, price, quantity, category)
#         self.size = size
#         self.material = material
#         self.color = color

#     def info(self):
#         print("Название:", self.name)
#         print("Цена:", self.price)
#         print("Количество:", self.quantity)
#         print("Категория:", self.category)
#         print("Размер:", self.size)
#         print("Материал:", self.material)
#         print("Цвет:", self.color)


# class Food(Product):
#     def __init__(self, name, price, quantity, category, expiration, weight):
#         super().__init__(name, price, quantity, category)
#         self.expiration = expiration
#         self.weight = weight

#     def info(self):
#         print("Название:", self.name)
#         print("Цена:", self.price)
#         print("Количество:", self.quantity)
#         print("Категория:", self.category)
#         print("Срок годности:", self.expiration)
#         print("Вес:", self.weight, "кг")


# product1 = Electronics(
#     "Телефон", 50000, 5, "Электроника", 12, "Samsung"
# )

# product2 = Clothes(
#     "Платье", 1500, 10, "Одежда", "M", "Хлопок", "Чёрный"
# )

# product3 = Food(
#     "Сыр", 100, 20, "Продукты", "25.08.2026", 1
# )

# products = [product1, product2, product3]

# for product in products:
#     product.info()
#     print()

# 3.
# class User:
#     def __init__(self, name, balance=0):
#         self.name = name
#         self.__balance = 0
#         self.deposit(balance)

#     @property
#     def balance(self):
#         return self.__balance

#     def deposit(self, amount):
#         if amount < 0:
#             raise ValueError("Баланс не может быть отрицательным")

#         self.__balance += amount

#     def withdraw(self, amount):
#         if amount <= 0:
#             raise ValueError("Сумма должна быть положительной")

#         if amount > self.__balance:
#             raise ValueError("Недостаточно средств")

#         self.__balance -= amount
        
# from abc import ABC, abstractmethod


# class Product(ABC):
#     def __init__(self, name, price, quantity):
#         if price < 0:
#             raise ValueError("Цена не может быть отрицательной")

#         if quantity < 0:
#             raise ValueError("Количество не может быть отрицательным")

#         self.name = name
#         self.__price = price
#         self.__quantity = quantity

#     @property
#     def price(self):
#         return self.__price

#     @property
#     def quantity(self):
#         return self.__quantity

#     def set_price(self, price):
#         if price < 0:
#             raise ValueError("Цена не может быть отрицательной")

#         self.__price = price

#     def increase_quantity(self, amount):
#         if amount <= 0:
#             raise ValueError("Количество должно быть положительным")

#         self.__quantity += amount

#     def decrease_quantity(self, amount):
#         if amount <= 0:
#             raise ValueError("Количество должно быть положительным")

#         if amount > self.__quantity:
#             raise ValueError("Недостаточно товара на складе")

#         self.__quantity -= amount

    # @abstractmethod
    # def get_category(self):
    #     pass

# class Electronics(Product):

#     def get_category(self):
#         return "Электроника"

#     def get_discount(self):
#         return 10

# class Clothing(Product):

#     def get_category(self):
#         return "Одежда"

#     def get_discount(self):
#         return 20

# class Food(Product):

#     def get_category(self):
#         return "Продукты"

#     def get_discount(self):
#         return 5

# class Order:
#     def __init__(self, user):
#         self.user = user
#         self.products = []
#         self.status = "Создан"

#     def add_product(self, product):
#         if product.quantity <= 0:
#             print("Товара нет в наличии")
#             return

#         product.decrease_quantity(1)
#         self.products.append(product)

#         print("Товар добавлен в заказ")

#     def calculate_total(self):
#         total = 0

#         for product in self.products:
#             total += product.price

#         return total

#     def pay(self):
#         price = self.calculate_total()

#         self.user.withdraw(price)

#         self.status = "Оплачен"

#     def ship(self):
#         self.status = "Отправлен"

#     def complete(self):
#         self.status = "Завершён"

# print("=" * 50)
# print("СОЗДАНИЕ ПОЛЬЗОВАТЕЛЕЙ")
# print("=" * 50)

# user1 = User("Байтур", 1000)
# user2 = User("Алмаз", 500)

# print(
#     f"Пользователь: {user1.name}, "
#     f"баланс: {user1.balance}"
# )

# print(
#     f"Пользователь: {user2.name}, "
#     f"баланс: {user2.balance}"
# )

# print("\n" + "=" * 50)
# print("ПОПОЛНЕНИЕ БАЛАНСА")
# print("=" * 50)

# user1.deposit(1000)
# print(
#     f"Баланс {user1.name}: "
#     f"{user1.balance}"
# )

# phone = Electronics("Телефон", 1000, 5)
# laptop = Electronics("Ноутбук", 1500, 3)

# jacket = Clothing("Куртка", 200, 10)
# tshirt = Clothing("Футболка", 50, 20)

# bread = Food("Хлеб", 5, 30)
# milk = Food("Молоко", 3, 20)

# print(
#     f"{phone.name} | "
#     f"{phone.get_category()} | "
#     f"Цена: {phone.price} | "
#     f"Количество: {phone.quantity}"
# )

# print(
#     f"{jacket.name} | "
#     f"{jacket.get_category()} | "
#     f"Цена: {jacket.price} | "
#     f"Количество: {jacket.quantity}"
# )

# print(
#     f"{bread.name} | "
#     f"{bread.get_category()} | "
#     f"Цена: {bread.price} | "
#     f"Количество: {bread.quantity}"
# )

# print(f"{phone.name}: {phone.get_discount()}%")
# print(f"{jacket.name}: {jacket.get_discount()}%")
# print(f"{bread.name}: {bread.get_discount()}%")

# print(f"Цена телефона со скидкой: {phone.get_final_price()}")
# print(f"Цена куртки со скидкой: {jacket.get_final_price()}")
# print(f"Цена хлеба со скидкой: {bread.get_final_price()}")

# order1 = Order(user1)

# order1.add_product(phone)
# order1.add_product(jacket)
# order1.add_product(bread)

# print(f"Стоимость без скидки: {order1.calculate_total()}")

# print(f"Телефонов осталось: {phone.quantity}")
# print(f"Курток осталось: {jacket.quantity}")
# print(f"Хлеба осталось: {bread.quantity}")

# print(f"Ноутбуков было: {laptop.quantity}")

# laptop.decrease_quantity(1)

# print(f"После уменьшения: {laptop.quantity}")

# laptop.increase_quantity(5)

# print(f"После пополнения склада: {laptop.quantity}")

# print(f"Баланс до оплаты: {user1.balance}")

# order1.pay()

# print(f"Баланс после оплаты: {user1.balance}")
# print(f"Статус заказа: {order1.status}")

# order1.ship()

# print(f"Статус: {order1.status}")

# order1.complete()

# print(f"Статус: {order1.status}")

# order2 = Order(user2)

# order2.add_product(tshirt)
# order2.add_product(milk)

# print(f"Стоимость второго заказа: {order2.calculate_total()}")

# try:
#     phone.set_price(-500)
# except ValueError as error:
#     print(f"Ошибка при изменении цены: {error}")

# try:
#     user2.withdraw(10000)
# except ValueError as error:
#     print(f"Ошибка при списании денег: {error}")

# try:
#     bread.decrease_quantity(1000)
# except ValueError as error:
#     print(f"Ошибка при изменении количества: {error}")

# try:
#     empty_product = Food("Товар закончился", 100, 0)
#     order2.add_product(empty_product)
# except ValueError as error:
#     print(f"Ошибка при добавлении товара: {error}")

# try:
#     bad_product = Electronics("Плохой товар", -100, 5)
# except ValueError as error:
#     print(f"Ошибка при создании товара: {error}")





