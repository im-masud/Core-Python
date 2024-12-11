def add_contact(contacts, name, email, phone, address):
    if any(contact['phone'] == phone for contact in contacts):
        print("\nPhone number already exists!")
        return False
    contacts.append({"name": name, "email": email, "phone": phone, "address": address})
    print("\nContact added successfully.")
    return True