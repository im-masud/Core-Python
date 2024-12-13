import add_books
import view_all_books
import restore_books
from datetime import datetime
import update_books, delete_books, lend_books, return_books


all_books = []


while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add Books")
    print("2. View All Books")
    print("3. Update Book")
    print("4. Remove Book")
    print("5. Lend Book") 
    print("6. Return Book")

    all_books = restore_books.restore_all_books(all_books)
    
    menu = input("Select any number: ")
    
    if menu.upper() == "Q":
        print("Thanks for using Library Management System ")
        break
    elif menu == "1":
        all_books = add_books.add_books(all_books)
    elif menu == "2":
        view_all_books.view_all_books(all_books)
    elif menu == "3":
        all_books = update_books.update_books(all_books)
    elif menu == "4":
        all_books = delete_books.delete_books(all_books)
    elif menu == "5":
        all_books = lend_books.lend_book(all_books)
    elif menu == "6":
        all_books = return_books.return_book(all_books)
    else:
        print("Choose a valid number")
