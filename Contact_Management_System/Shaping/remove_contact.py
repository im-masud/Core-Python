def remove_contact(contacts, phone):
    for contact in contacts:
        if contact['phone'] == phone:
            contacts.remove(contact)
            print("\nContact removed successfully.")
            return True
    print("\nContact Ghurte Gase!")
    return False