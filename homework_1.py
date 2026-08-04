class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def get_info(self):
        print(f"Книга: {self.title} автор: {self.author} страниц: {self.pages}")
    def read(self, pages_read):
        print(f"Прочитано {pages_read} из {self.pages} страниц")

book = Book("The Master and Margarita", "Mikhail Bulgakov", 448)
book.get_info()
book.read(167)