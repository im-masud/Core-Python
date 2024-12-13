import json
from datetime import datetime
import save_all_books

def return_book(all_books):
    book_title = input("Enter Book Title to Return: ")
    borrower_name = input("Enter Borrower's Name: ")

    
    try:
        with open("lent_books.json", "r") as fp:
            lent_books = json.load(fp)
    except (json.JSONDecodeError, FileNotFoundError):
        print("Lent books file is empty or corrupted.")
        return all_books

    
    if not isinstance(lent_books, list):
        print("Lent books data is not a list. Resetting lent_books.json.")
        lent_books = []

    
    for lend_info in lent_books:
        if lend_info["book_title"].lower() == book_title.lower() and lend_info["borrower_name"].lower() == borrower_name.lower():
            
            lent_books.remove(lend_info)

            
            for book in all_books:
                if book["title"].lower() == book_title.lower():
                    book["quantity"] += 1
                    break
            
            
            save_all_books.save_all_books(all_books)

            
            with open("lent_books.json", "w") as fp:
                json.dump(lent_books, fp, indent=4)

            print(f"Book returned by {borrower_name} successfully!")
            return all_books
    
    print("No record found for this book and borrower.")
    return all_books
