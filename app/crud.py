from sqlalchemy.orm import Session
from app.models import Contact

def create_contact(db: Session, name: str, phone: str, email: str) -> Contact:
    new_contact = Contact(name=name, phone_number=phone, email=email)
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

def get_all_contacts(db: Session):
    return db.query(Contact).all()

def update_contact(db: Session, contact_id: int, name: str, phone: str, email: str) -> Contact:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.name = name
        contact.phone_number = phone
        contact.email = email
        db.commit()
        db.refresh(contact)
        return contact
    return None

def delete_contact(db: Session, contact_id: int) -> bool:
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
        return True
    return False
