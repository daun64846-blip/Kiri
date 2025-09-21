class Book:
    def __init__(self, title, author, publication_year):
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def display_info(self):
        print(f"Назва: {self.title}")
        print(f"Автор: {self.author}")
        print(f"Рік видання: {self.publication_year}")

class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print(f"Книги в бібліотеці '{self.name}':")

    book1 = Book("Гаррі Поттер і філософський камінь", "Джоан Роулінг", 1997)
    book2 = Book("Володар перснів: Братство персня", "Дж. Р. Р. Толкін", 1954)
    book3 = Book("Маленький принц", "Антуан де Сент-Екзюпері", 1943)

    my_library = Library("Центральна міська бібліотека")

    my_library.add_book(book1)
    my_library.add_book(book2)
    my_library.add_book(book3)

    my_library.display_books()



