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
    try:
        if os.path.exists(filename):
            with open(filename,"r") as file:
                lines=file.readlines()
                if lines:
                    print("Contacts in the inventory: ")
                    for line in lines:
                        try:
                            name,num=line.strip().split(',')
                            file.append({"name": name, "number": num})
                            print(f"Contact name: {name}, Contact number: {num}")
                        except ValueError:
                            print(f"Skipping malfunction line: {line.strip()}")
                else:
                    print("Inventory is empty.")
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print("An error occurred: ",e)

def save(filename,contacts):
    try:
        with open(filename,"w") as file:
            name, num = contact.strip().split(',')
            contact=f"Contact name: {name}, Contact number: {num}"
            for contact in contacts:
                file.write()
        print("Contacts have been saved.")
    except Exception as e:
        print("An error occurred: ",e)
    
def add(filename):
    try:
        with open(filename, "a") as file:
            name = input("Enter the contact's name: ")
            num = input("Enter the contact's number: ")
            contact = f"{name}, {num}\n"
            file.write(contact)
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
                
def update(filename):
    try:
        if os.path.exists(filename):
            name_to_update = input("Enter the name of the contact to update: ")
            contacts = load(filename) 
            for contact in contacts:
                if contact['name'] == name_to_update:
                    new_number = input(f"Enter the new number for {name_to_update}: ")
                    contact['number'] = new_number
                    save(filename, contacts)
                    print("Contact has been updated.")
                    return
            print("Contact not found.")
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print("An error occurred while updating the contact:", e)

def delete(filename):
    try:
        if os.path.exists(filename):
            name_to_delete = input("Enter the name of the contact to delete: ").lower()
            contacts = load(filename)  
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
        else:
            print("Inventory file does not exist.")
    except Exception as e:
        print("An error occurred:", e)

def main():
    filename="contacts.txt"
    contacts=[]
    while True:
        display()
        choice=input("Enter your choice: ")
        if choice=="1":
            load(filename)
        elif choice=="2":
            save(filename,contacts)
        elif choice=="3":
            add(filename)
        elif choice=="4":
            view(filename)
        elif choice=="5":
            update(filename)
        elif choice=="6":
            delete(filename)
        elif choice=="7":
            print("Exiting the code.")  
            break  
        else:
            print("Invalid choice.")    

if __name__=="__main__":
    main()
