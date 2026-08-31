class Book:

    def __init__(self, book_id, title, author, year, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.is_available = True

    def add_book(self):
        print(f"Книга '{self.title}' добавлена.")

    def change_book(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        print(f"Книга '{self.title}' изменена.")

    def delete_book(self):
        print(f"Книга '{self.title}' удалена.")

    def get_info(self):
        return (
            f"Id: {self.book_id}\n"
            f"Название: {self.title}\n"
            f"Автор: {self.author}\n"
            f"Год издания: {self.year}\n"
            f"Жанр: {self.genre}\n"
            f"Доступность: {'Да' if self.is_available else 'Нет'}"
        )

    def check_availability(self):
        return self.is_available