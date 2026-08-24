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