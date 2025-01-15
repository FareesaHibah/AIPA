import os

def display():
    print("Welcome to CONTACT MANAGEMENT SYSTEM!")
    print("1. Load contacts from a file")
    print("2. Save contacts to a file")
    print("3. Add a contact")
    print("4. View all contacts")
    print("5. Update a contact")
    print("6. Delete a contact")
    print("7. Exit")

def load(filename):
    contacts = []
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                lines = file.readlines()
                if lines:
                    print("Contacts in the inventory: ")
                    for line in lines:
                        try:
                            name, num = line.strip().split(',')
                            contacts.append({"name": name, "number": num})
                            print(f"Contact name: {name}, Contact number: {num}")
                        except ValueError:
                            print(f"Skipping malfunction line: {line.strip()}")
                else:
                    print("Inventory is empty.")
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print("An error occurred:", e)
    return contacts

def save(filename, contacts):
    try:
        with open(filename, "w") as file:
            for contact in contacts:
                file.write(f"{contact['name']},{contact['number']}\n")
        print("Contacts have been saved.")
    except Exception as e:
        print("An error occurred:", e)

def add(filename, contacts):
    try:
        name = input("Enter the contact's name: ")
        num = input("Enter the contact's number: ")
        contacts.append({"name": name, "number": num})
        save(filename, contacts)
        print("Contact has been added.")
    except Exception as e:
        print("An error occurred:", e)

def view(filename):
    try:
        if os.path.exists(filename):
            with open(filename, "r") as file:
                contacts = file.readlines()
                if contacts:
                    print("Contacts in the inventory:")
                    for contact in contacts:
                        try:
                            name, num = contact.strip().split(',')
                            print(f"Contact name: {name}, Contact number: {num}")
                        except ValueError:
                            print(f"Skipping malfunction line: {contact.strip()}")
                else:
                    print("Inventory is empty.")
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print("An error occurred:", e)

def update(filename, contacts):
    try:
        name_to_update = input("Enter the name of the contact to update: ")
        for contact in contacts:
            if contact['name'] == name_to_update:
                new_number = input(f"Enter the new number for {name_to_update}: ")
                contact['number'] = new_number
                save(filename, contacts)
                print("Contact has been updated.")
                return
        print("Contact not found.")
    except Exception as e:
        print("An error occurred while updating the contact:", e)

def delete(filename, contacts):
    try:
        name_to_delete = input("Enter the name of the contact to delete: ").lower()
        found = False
        for contact in contacts:
            if contact['name'].lower() == name_to_delete:
                contacts.remove(contact)
                save(filename, contacts)
                print(f"Deleted - {contact['name']}, Number: {contact['number']}")
                found = True
                break
        if not found:
            print("Contact not found.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    filename = "contacts.txt"
    contacts = load(filename)  # Load contacts initially from file
    while True:
        display()
        choice = input("Enter your choice: ")
        if choice == "1":
            contacts = load(filename)
        elif choice == "2":
            save(filename, contacts)
        elif choice == "3":
            add(filename, contacts)
        elif choice == "4":
            view(filename)
        elif choice == "5":
            update(filename, contacts)
        elif choice == "6":
            delete(filename, contacts)
        elif choice == "7":
            print("Exiting the code.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
