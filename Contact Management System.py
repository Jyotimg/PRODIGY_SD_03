
### Complete Implementation: main.py

```python
import json
import os

# Define the file name for persistent storage
FILE_NAME = 'contacts.json'

# Load contacts from the file if it exists
def load_contacts():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    return []

# Save contacts to the file
def save_contacts():
    with open(FILE_NAME, 'w') as file:
        json.dump(contacts, file)

contacts = load_contacts()

def display_menu():
    print("\nContact Management System")
    print("1. Add New Contact")
    print("2. View Contacts")
    print("3. Edit Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts()
    print("Contact added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts, start=1):
            print(f"{idx}. {contact['name']} - {contact['phone']} - {contact['email']}")

def edit_contact():
    view_contacts()
    index = int(input("Enter the number of the contact to edit: ")) - 1
    if 0 <= index < len(contacts):
        contacts[index]['name'] = input("Enter new name: ")
        contacts[index]['phone'] = input("Enter new phone number: ")
        contacts[index]['email'] = input("Enter new email address: ")
        save_contacts()
        print("Contact updated successfully!")
    else:
        print("Invalid contact number.")

def delete_contact():
    view_contacts()
    index = int(input("Enter the number of the contact to delete: ")) - 1
    if 0 <= index < len(contacts):
        contacts.pop(index)
        save_contacts()
        print("Contact deleted successfully!")
    else:
        print("Invalid contact number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            edit_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
