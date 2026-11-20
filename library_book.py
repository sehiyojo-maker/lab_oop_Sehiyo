
class Book:
    book_count = 0

    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

        Book.book_count += 1

    def borrow(self):
        if self.available:
            self.available = False
            print(f"You borrowed '{self.title}'.")
        else:
            print(f"'{self.title}' is already borrowed.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"You returned '{self.title}'.")
        else:
            print(f"'{self.title}' is already available.")

    def __str__(self):
        status = "Available" if self.available else "Borrowed"
        return f"{self.title} by {self.author} - {status}"

    def __repr__(self):
        return (f"Book(title={self.title!r}, "
                f"author={self.author!r})")


# Creating book objects
book1 = Book("Python Basics", "John Smith")
book2 = Book("Introduction to Programming", "Mary Cruz")
book3 = Book("Learning OOP", "David Santos")


# Displaying all books
print("LIBRARY BOOK COLLECTION")
print(book1)
print(book2)
print(book3)

# Borrowing books
print("\nBORROWING BOOKS")
book1.borrow()
book2.borrow()

# Trying to borrow an already borrowed book
book1.borrow()

# Returning a book
print("\nRETURNING BOOKS")
book1.return_book()

# Displaying updated information
print("\nUPDATED BOOK COLLECTION")
print(book1)
print(book2)
print(book3)

# Displaying total number of books
print("\nTotal books:", Book.book_count)

# Displaying developer representation
print("\nBOOK REPRESENTATION")
print(repr(book1))
