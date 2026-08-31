class User:

    def __init__(self, user_id, name, email):
        self.user_id = user_id
        self.name = name
        self.email = email

    def get_info(self):
        return (
            f"Id: {self.user_id}\n"
            f"Имя: {self.name}\n"
            f"Email: {self.email}"
        )

    def take_book(self, book):
        if book.check_availability():
            book.is_available = False
            print(f"{self.name} взял книгу '{book.title}'.")
        else:
            print("Книга уже выдана.")

    def return_book(self, book):
        book.is_available = True
        print(f"{self.name} вернул книгу '{book.title}'.")