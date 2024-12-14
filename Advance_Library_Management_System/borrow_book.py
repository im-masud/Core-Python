import save_all_books

def borrow_book(all_info):
    book_title = input("Enter book title: ")
    borrower_name = input("Enter your name: ").upper()
    phone_number = int(input("Enter your phone number: "))
    due_date = int(input("Enter due date (YYYY-MM-DD): "))
    
    for book in all_info:
        if book['title'] == book_title:
            if book['quantity'] > 0:
                book['quantity'] -= 1
                for item in all_info:
                    if item.get("title") == book_title:
                        item["additional_info"] = {
                        'name': borrower_name,
                        'phone': phone_number,
                        'due_date': due_date
                        }           
                        save_all_books.save_all_books(all_info)
                        print(f"Book '{book_title}' borrowed successfully.")
                        return
        else:
            print(f"Sorry, '{book_title}' is currently out of stock.")
            return
    print(f"Book '{book_title}' not found.")
