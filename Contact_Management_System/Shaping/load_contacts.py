import csv

def load_contacts(file_path):
    try:
        with open(file_path, "r") as file:
            reader = csv.DictReader(file)
            return [row for row in reader]
    except FileNotFoundError:
        return []