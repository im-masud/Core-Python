def search_contact(contacts, keyword):
    results = [contact for contact in contacts if keyword.lower() in contact['name'].lower() or
            keyword in contact['email'] or keyword in contact['phone']]
    if results:
        print("\nSearch Results:")
        for contact in results:
            print(f"\nName: {contact['name']}, Email: {contact['email']}, Phone: {contact['phone']}, Address: {contact['address']}")
    else:
        print("\nNo contact found.")