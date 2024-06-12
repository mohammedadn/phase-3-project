from app.database import SessionLocal
from app.crud import create_contact, get_all_contacts, update_contact, delete_contact


def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    email = input("Enter email: ")
    db = SessionLocal()
    contact = create_contact(db, name, phone, email)
    if contact:
        print(f"Contact added: {contact.name}, {contact.phone_number}, {contact.email}")
    else:
        print("Failed to add contact. Please try again.")
    db.close()

def list_contacts():
    db = SessionLocal()
    contacts = get_all_contacts(db)
    for contact in contacts:
        print(f"ID: {contact.id}, Name: {contact.name}, Phone: {contact.phone_number}, Email: {contact.email}")
    db.close()

def edit_contact():
    contact_id = int(input("Enter contact ID: "))
    name = input("Enter new name: ")
    phone = input("Enter new phone: ")
    email = input("Enter new email: ")
    db = SessionLocal()
    contact = update_contact(db, contact_id, name, phone, email)
    if contact:
        print(f"Contact updated: {contact.name}, {contact.phone_number}, {contact.email}")
    else:
        print("Contact not found.")
    db.close()

def remove_contact():
    contact_id = int(input("Enter contact ID: "))
    db = SessionLocal()
    contact = delete_contact(db, contact_id)
    if contact:
        print("Contact deleted.")
    else:
        print("Contact not found.")
    db.close()

def main():
    while True:
        print("1. Add Contact")
        print("2. List Contacts")
        print("3. Edit Contact")
        print("4. Remove Contact")
        print("5. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            add_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            edit_contact()
        elif choice == "4":
            remove_contact()
        elif choice == "5":
            break
        else:
            print("Invalid option. Try again.")

if __name__ == "__main__":
    main()
