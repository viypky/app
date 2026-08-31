import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
if current_dir not in sys.path:
    sys.path.insert(0, current_dir)

from models.book import Book
from models.user import User
from models.admin import Admin
from services.library import Library
from database.connection import create_tables


def main():
    create_tables()
    print("База данных создана")
    print()

    library = Library()

    book = Book(
        1,
        "Преступление и наказание",
        "Фёдор Достоевский",
        1867,
        "Роман"
    )

    user = User(
        1,
        "Али",
        "ali@email.com"
    )

    admin = Admin(
        2,
        "Админ",
        "admin@email.com"
    )

    library.add_book(book)
    library.add_user(user)

    print(book.get_info())
    print()
    print(user.get_info())
    print()

    user.take_book(book)
    print("Доступна:", book.check_availability())

    user.return_book(book)
    print("Доступна:", book.check_availability())

    admin.get_statistics()

    print("\nMRO:")
    for item in Book.__mro__:
        print(item)

if __name__ == "__main__":
    main()
