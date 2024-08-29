# Create classes Library, Borrower and Book
# Add the different methods into each class
# Add, borrow and return books
# We can search for books in the library

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False

    def borrow_book(self):
        if not self.is_borrowed:
            return f"You have successfully borrowed '{self.title}'."
        else:
            return f"Sorry, '{self.title}' is already borrowed."

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            return f"You have successfully returned '{self.title}'."
        else:
            return f"'{self.title}' wasn't borrowed."

class Borrower:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []

    def borrow_book(self, book):
        if book.is_borrowed:
            return f"Sorry, '{book.title}' is already borrowed."
        else:
            book.borrow_book()
            self.borrowed_books.append(book)
            return f"{self.name} borrowed '{book.title}'."

    def return_book(self, book):
        if book in self.borrowed_books:
            book.return_book()
            self.borrowed_books.remove(book)
            return f"{self.name} returned '{book.title}'."
        else:
            return f"{self.name} hasn't borrowed '{book.title}'."

    def list_borrowed_books(self):
        if not self.borrowed_books:
            return f"{self.name} has no borrowed books."
        return f"{self.name} has borrowed: " + ", ".join(book.title for book in self.borrowed_books)

class Library:
    def __init__(self):
        self.books = []
        self.borrowers = []

    def add_book(self, book):
        self.books.append(book)
        return f"Added '{book.title}' to the library."

    def add_borrower(self, borrower):
        self.borrowers.append(borrower)
        return f"Added borrower '{borrower.name}'."

    def lend_book(self, borrower, book):
        if book not in self.books:
            return f"'{borrower.name}' is not registered as a borrower."
        return borrower.borrow_book(book)

    def return_book(self, borrower, book):
        if borrower not in self.borrowers:
            return f"'{borrower.name}' is not registered as a borrower."
        return borrower.return_book(book)

    def list_available_books(self):
        available_books = [book for book in self.books if not book.is_borrowed]
        if not available_books:
            return "No books are available at this time."
        return "Available books: " + ", ".join(book.title for book in available_books)

    def search_books(self, search_query):
        results = [book for book in self.books if search_query.lower() in book.title.lower() or search_query.lower() in book.author.lower()]
        if not results:
            return f"No books found for query '{search_query}'."
        return f"Search results for '{search_query}': " + ", ".join(book.title for book in results)


# Example Usage
if __name__ == "__main__":
    # Create a library
    library = Library()

    # Add 20 books to the library
    books = [
        Book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890"),
        Book("1984", "George Orwell", "2345678901"),
        Book("To Kill a Mockingbird", "Harper Lee", "3456789012"),
        Book("Moby Dick", "Herman Melville", "4567890123"),
        Book("War and Peace", "Leo Tolstoy", "5678901234"),
        Book("Pride and Prejudice", "Jane Austen", "6789012345"),
        Book("The Catcher in the Rye", "J.D. Salinger", "7890123456"),
        Book("The Hobbit", "J.R.R. Tolkien", "8901234567"),
        Book("Fahrenheit 451", "Ray Bradbury", "9012345678"),
        Book("Jane Eyre", "Charlotte Brontë", "1123456789"),
        Book("The Odyssey", "Homer", "2234567890"),
        Book("Brave New World", "Aldous Huxley", "3345678901"),
        Book("The Iliad", "Homer", "4456789012"),
        Book("Crime and Punishment", "Fyodor Dostoevsky", "5567890123"),
        Book("The Lord of the Rings", "J.R.R. Tolkien", "6678901234"),
        Book("The Alchemist", "Paulo Coelho", "7789012345"),
        Book("The Divine Comedy", "Dante Alighieri", "8890123456"),
        Book("The Brothers Karamazov", "Fyodor Dostoevsky", "9901234567"),
        Book("Don Quixote", "Miguel de Cervantes", "0012345678"),
        Book("Ulysses", "James Joyce", "0123456789")
    ]
    for book in books:
        library.add_book(book)

    # Add 10 borrowers to the library
    borrowers = [
        Borrower("Alice"),
        Borrower("Bob"),
        Borrower("Charlie"),
        Borrower("David"),
        Borrower("Eve"),
        Borrower("Frank"),
        Borrower("Grace"),
        Borrower("Hannah"),
        Borrower("Ivy"),
        Borrower("Jack")
    ]
    for borrower in borrowers:
        library.add_borrower(borrower)

    # Borrow a few books
    print(library.lend_book(borrowers[0], books[0]))  # Alice borrows The Great Gatsby
    print(library.lend_book(borrowers[1], books[1]))  # Bob borrows 1984
    print(library.lend_book(borrowers[2], books[2]))  # Charlie borrows To Kill a Mockingbird
    print(library.lend_book(borrowers[3], books[3]))  # David borrows Moby Dick

    # List available books
    print(library.list_available_books())

    # Return a book
    print(library.return_book(borrowers[0], books[0]))  # Alice returns The Great Gatsby

    # List borrowed books
    print(borrowers[0].list_borrowed_books())  # Alice
    print(borrowers[1].list_borrowed_books())  # Bob
    print(borrowers[2].list_borrowed_books())
    print(borrowers[3].list_borrowed_books())

    # Search books by title or author
    print(library.search_books("George Orwell"))
    print(library.search_books("Dostoevsky"))
    print(library.search_books("James Joyce"))
