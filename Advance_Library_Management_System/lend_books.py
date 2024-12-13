import json
from datetime import datetime
import save_all_books

def lend_book(all_books):
    book_title = input("Enter Book Title to Lend: ")
    borrower_name = input("Enter Borrower's Name: ")
    borrower_phone = input("Enter Borrower's Phone Number: ")

    for book in all_books:
        if book["title"].lower() == book_title.lower():
            if book["quantity"] > 0:
                due_date = input("Enter Due Date (DD-MM-YYYY): ")
                try:
                    due_date = datetime.strptime(due_date, "%d-%m-%Y")
                except ValueError:
                    print("Invalid date format!")
                    return all_books

                book["quantity"] -= 1

                lend_info = {
                    "borrower_name": borrower_name,
                    "borrower_phone": borrower_phone,
                    "book_title": book_title,
                    "lend_date": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
                    "due_date": due_date.strftime("%d-%m-%Y")
                }
                

                try:
                    with open("lent_books.json", "r") as fp:
                        lent_books = json.load(fp)
                except (json.JSONDecodeError, FileNotFoundError):
                    lent_books = []

                
                lent_books.append(lend_info)

                
                with open("lent_books.json", "w") as fp:
                    json.dump(lent_books, fp, indent=4)
                
                
                save_all_books.save_all_books(all_books)
                print(f"Book lent to {borrower_name} successfully!")
                return all_books
            else:
                print("There are not enough books available to lend.")
                return all_books
    
    print("Book not found.")
    return all_books
