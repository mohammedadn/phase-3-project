from app.database import init_db, SessionLocal
from app.crud import create_contact, get_all_contacts, get_contact_by_id, update_contact, delete_contact

def main():

    init_db()


    db = SessionLocal()


    contact = create_contact(db, "Mark Kamamia", "07191281912", "markmaina@gmail.com")
    print(F"contact made: {contact.name}, {contact.phone}, {contact.email}")

    contacts = get_all_contacts(db)
    for contact in contacts:
        print(F"Contact ID: {contact.id}, Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}, ")


    db.close()

if __name__ == "__main__":        

    main()