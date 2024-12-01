import csv

def save_contacts(file_path, contacts):
    with open(file_path, "w", newline="") as file:
        fieldnames = ["name", "email", "phone", "address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
