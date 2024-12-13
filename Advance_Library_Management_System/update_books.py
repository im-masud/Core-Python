import save_all_books
from datetime import datetime

def update_books(all_books):
    search_book = input("Enter Book Title to Update: ")
    for book in all_books:
        if book["title"].lower() == search_book.lower():
            print(f"Current details: {book}")
            title = input(f"Enter new title (current: {book['title']}): ") or book['title']
            author = input(f"Enter new author (current: {book['author']}): ") or book['author']
            year = int(input(f"Enter new publishing year (current: {book['year']}): ") or book['year'])
            price = int(input(f"Enter new price (current: {book['price']}): ") or book['price'])
            quantity = int(input(f"Enter new quantity (current: {book['quantity']}): ") or book['quantity'])

            book_last_updated_at = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

            book.update({
                "title": title,
                "author": author,
                "year": year,
                "price": price,
                "quantity": quantity,
                "bookLastUpdatedAt": book_last_updated_at
            })

            save_all_books.save_all_books(all_books)
            print("Book Updated Successfully")
            return all_books

    print("Book Not Found")
    return all_books
