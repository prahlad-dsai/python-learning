import json
class Book:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def display_string(self)->str:
        status = "Available" if self.available else "Checked out"
        return f"'{self.title}' by {self.author} — {status}"


class Library:
    def load_books(self):
        try:
            with open("books.json", "r") as file:
                data = json.load(file)

            for book_data in data:
                book = Book(
                    book_data["title"],
                    book_data["author"]
                )
                book.available = book_data["available"]
                self.books.append(book)

        except FileNotFoundError:
            self.books = []
    def __init__(self):
        self.books = []

    def add_book(self):
        title = input("Title: ")
        author = input("Author: ")
        self.books.append(Book(title, author))
        self.save_books()
        print("Book Added!\n")

    def view_books(self):
        if not self.books:
            print("No books in the library.\n")
            return
        for index, book in enumerate(self.books, start=1):
            print(f"{index}. {book.display_string()}")
        print()

    def search_book(self):
        title = input("Enter the title of the book: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"{book.display_string()}")
                print()
                return
        print("Book not found.\n")

    def borrow_book(self):
       title = input("Enter title to borrow: ")
       for book in self.books:
           if book.title.lower() == title.lower():
               if book.available:
                   book.available = False
                   self.save_books()
                   print(f"You've borrowed '{book.title}'.\n")
               else:
                   print(f"'{book.title}' is currently not available.\n")
               return
       print("Book not found.\n")

    def return_book(self):
        title = input("Enter title to return: ")
        for book in self.books:
            if book.title.lower() == title.lower():
                if not book.available:
                    book.available = True
                    self.save_books()
                    print(f"You've returned '{book.title}'.\n")
                else:
                    print(f"'{book.title}' was not borrowed.\n")
                return
        print("Book not found.\n")

    def save_books(self):
        data = []

        for book in self.books:
            data.append({
                "title": book.title,
                "author": book.author,
                "available": book.available
            })

        with open("books.json", "w") as file:
            json.dump(data, file, indent=4)
    def remove_book(self):
        title = input("Enter the title of the book to remove: ")

        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                self.save_books()
                print("Book removed successfully.\n")
                return

        print("Book not found.\n")


def main():
    library = Library()
    library.load_books()

    while True:
        print("--- Library Management System ---")
        print("1. Add book")
        print("2. View books")
        print("3. Search book")
        print("4. Borrow book")
        print("5. Return book")
        print("6. Remove book")
        print("7. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            library.add_book()
        elif choice == "2":
            library.view_books()
        elif choice == "3":
            library.search_book()
        elif choice == "4":
            library.borrow_book()
        elif choice == "5":
            library.return_book()
        elif choice == "6":
            library.remove_book()
        elif choice == "7":
            print("Goodbye.Thank you.Please visit again.")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()

