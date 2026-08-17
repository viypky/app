# class Cat:
#     def eat(self):
#         print("eat")

#     def sleep(self):
#         print("sleep")

# class Cat(Animal):
#     pass

# class Dog(Animal):
#     pass

# HAS - A = car -> engine
# IS - A = Veh

# class Engine:
#     pass

# class Car: #наследование
#     def __init__(self):
#         self.engine = Engine() #композиция

# class Bird:
#     def fly (self):
#         print("fly")

# class Penguin(Bird):
#     pass

# class Owl(Bird):
#     pass

# 01 = Owl()
# 01.fly()

# class Animal:
#     pass

# class Dog(Animal):
#     pass

# print(Dog.__mro__)

# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         print("Gav gav")

# class Cat(Animal):
#     def speak(self):
#             print("Meow meow")

# class Owl(Animal):
#     def speak(self):
#             print("Hoot hoot")

# class Mowse(Animal):
#     def speak(self):
#             print("Squeak squeak")

# def make_animal_speak(animal: Animal):
#      animal.speak()

# make_animal_speak(Dog())
# make_animal_speak(Cat())
# make_animal_speak(Owl())
# make_animal_speak(Mowse())

# class Payment:
#     def __init__(self, amount):
#         self.amount = amount

#     def pay(self):
#         print(f"Оплата на сумму {self.amount} прошла успешно")

# class Cardayment(Payment):
#     def pay(self):
#         print(f"Оплата картой : {self.amount}  прошла успешно") 

# class CashPayment(Payment):
#     def pay(self):
#         print(f"Оплата наличными : {self.amount}  прошла успешно") 


# class QRPayment(Payment):
#     def pay(self):
#         print(f"Оплата QR : {self.amount}  прошла успешно")   

# def checkout (payment: Payment):
#     payment.pay()

# payments = [
#     Cardayment(100)
#     CashPayment(200)
#     QRPayment(500)
# ]
