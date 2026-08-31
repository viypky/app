from models.user import User


class Admin(User):

    def add_book(self, book):
        book.add_book()

    def delete_book(self, book):
        book.delete_book()

    def change_book(self, book, title, author, year, genre):
        book.change_book(title, author, year, genre)

    def get_statistics(self):
        print("Просмотр статистики библиотеки.")