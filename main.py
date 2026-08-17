1.
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