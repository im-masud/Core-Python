def view_contacts(contacts):
    print("\nContacts:")
    for contact in contacts:
        print(f"\nName: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")