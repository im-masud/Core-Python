import os
import csv

class Library:
    def __init__(self, filename="library_books.csv"):
        self.filename = filename
        self.books = self.load_books()

    def load_books(self):
        """Load books from the file into the system."""
        if os.path.exists(self.filename):
            with open(self.filename, 'r', newline='') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                books = {row[2]: {'title': row[0], 'author': row[1], 'isbn': row[2], 'year': row[3], 'price': row[4], 'quantity': row[5]} for row in reader}
            return books
        return {}

    def save_books(self):
        """Save all the books to the file."""
        with open(self.filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['title', 'author', 'isbn', 'year', 'price', 'quantity'])  # Write the header
            for book in self.books.values():
                writer.writerow([book['title'], book['author'], book['isbn'], book['year'], book['price'], book['quantity']])

    def add_book(self, title, author, isbn, year, price, quantity):
        """Add a new book to the system."""
        self.books[isbn] = {'title': title, 'author': author, 'isbn': isbn, 'year': year, 'price': price, 'quantity': quantity}
        self.save_books()
        print("Book added successfully.")

    def update_book(self, isbn, title=None, author=None, year=None, price=None, quantity=None):
        """Update an existing book's details."""
        if isbn in self.books:
            book = self.books[isbn]
            if title: book['title'] = title
            if author: book['author'] = author
            if year: book['year'] = year
            if price: book['price'] = price
            if quantity: book['quantity'] = quantity
            self.save_books()
            print("Book updated successfully.")
        else:
            print("Book not found.")

    def remove_book(self, isbn):
        """Remove a book from the system."""
        if isbn in self.books:
            del self.books[isbn]
            self.save_books()
            print("Book removed successfully.")
        else:
            print("Book not found.")

    def view_books(self):
        """Display all books in the system."""
        if self.books:
            print("\nList of Books:")
            for isbn, book in self.books.items():
                print(f"ISBN: {isbn}, Title: {book['title']}, Author: {book['author']}, Year: {book['year']}, Price: {book['price']}, Quantity: {book['quantity']}")
        else:
            print("No books available.")

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View All Books")
        print("3. Update Book")
        print("4. Remove Book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            author = input("Enter author(s): ")
            isbn = input("Enter ISBN: ")
            year = input("Enter publishing year: ")
            price = input("Enter price: ")
            quantity = input("Enter quantity: ")
            library.add_book(title, author, isbn, year, price, quantity)

        elif choice == '2':
            library.view_books()

        elif choice == '3':
            isbn = input("Enter ISBN of the book to update: ")
            print("Enter new details (Leave blank to keep the current value):")
            title = input("New Title: ")
            author = input("New Author: ")
            year = input("New Year: ")
            price = input("New Price: ")
            quantity = input("New Quantity: ")

            # If the user leaves a field empty, it will not be updated
            library.update_book(isbn,
                                title if title else None,
                                author if author else None,
                                year if year else None,
                                price if price else None,
                                quantity if quantity else None)

        elif choice == '4':
            isbn = input("Enter ISBN of the book to remove: ")
            library.remove_book(isbn)

        elif choice == '5':
            print("Exiting the system.")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
