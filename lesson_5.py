
# class User:
#     role_default = "quest"

#     def __init__(self, name: str, age :int):
#         self.name = name
#         self.age = age

#     @classmethod
#     def from_string(cls, user_str : str):
#         name, age = user_str.split("-")
#         return cls(name, int(age))

#     @classmethod
#     def set_default_role(cls, new_role: str):
#         cls.role_default = new_role

# u1 = User("Алексей", 25)
# u2 = User.from_string("Bob-25")
# print(u2.name, u2.age)

# User.set_default_role("admin")
# print(u1.set_default_role, u2.role_default)

class DateValidator:
    def __init__(self, day, month, year):
       if not self.is_valid_date(day, month, year):
           raise ValueError("Некорректная дата")
       self.day = day
       self.month = month
       self.year = year

    @staticmethod
    def is_valid_date(day, month, year):
        if year < 1 or not (1 <= month <= 12):
            return False
        if not (1 <= day <= 31):
            return False
        return True

print(DateValidator.is_valid_date(32, 12, 2020))

