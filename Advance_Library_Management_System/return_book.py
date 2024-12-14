import save_all_books
def return_book(data):
    title = input("Enter Book Title to Return: ")
    name = input("Enter your name: ")
    phone = int(input("Enter your number: "))
    for book in data:
        if book["additional_info"]["phone"] == phone:
            del book["additional_info"]
            book["quantity"] += 1
            print(f"Thank you {name},You returnd secussfully this BOOK {title}")
            save_all_books.save_all_books(data)
            return data

    print("Book Not Found")