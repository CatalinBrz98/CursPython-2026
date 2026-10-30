from animale import Dog

class Book:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title: str, author: str, file_size: int, file_format: str):
        Book.__init__(self, title, author)
        self.file_size = file_size
        self.file_format = file_format

class Library:
    def __init__(self, books: list[Book | EBook]):
        self.books = books

    def books_count(self) -> int:
        return len(self.books)

    def total_digital_space(self) -> int:
        return sum([book.file_size for book in self.books if isinstance(book, EBook)])

if __name__ == "__main__":
    libraria_edu = Library([
        Book("Dog", ""),
        EBook("Mihai Spanu", "Mihaita Piticu", 2654, "txt"),
        Book("Cat", ""),
        EBook("Mihai Spanu", "Mihaita Piticu", 7362, "txt")
    ])

    print(libraria_edu.books_count())
    print(libraria_edu.total_digital_space())
