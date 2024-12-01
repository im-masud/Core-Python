import load_contacts
import save_contacts
import add_contact
import view_contacts
import search_contact
import remove_contact

file = "contacts.csv"
contacts = load_contacts.load_contacts(file)
while True:
    print("\nContact Book Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        try:
            name = input("Name: ")
            email = input("Email: ")
            phone = int(input("Phone: "))
            address = input("Address: ")
            if add_contact.add_contact(contacts, name, email, phone, address):
                save_contacts.save_contacts(file, contacts)
        except:
            print("\nEnter valid Number")
    elif choice == "2":
        view_contacts.view_contacts(contacts)
    elif choice == "3":
        keyword = input("Search by name, email, or phone: ")
        search_contact.search_contact(contacts, keyword)
    elif choice == "4":
        phone = input("Enter phone number to delete: ")
        if remove_contact(contacts, phone):
            save_contacts.save_contacts(file, contacts)
    elif choice == "5":
        print("\nHave a nice day...")
        break
    else:
        print("\nInvalid choice. Please try again.")
