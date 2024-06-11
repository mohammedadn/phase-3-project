from app.models import Contact
from sqlalchemy.orm import Session

def create_contact(db: Session, name:str, phone:str, email:str):
    contact = Contact(name=name, phone=phone, email=email)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

def get_all_contacts(db: Session):
    return db.query(Contact).all()

def get_contact_by_id(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()

def update_contact(db: Session, contact_id: int, name: str , phone:str, emial: str):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.name = name
        contact.phone = phone
        contact.email = email
        db.commit()
        db.refresh(contact)
    return contact

def delete_contact(db: Session, contact_id: int):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact    




"""

from app.models import Contact
from sqlalchemy.orm import Session

def create_contact(db: Session, name: str, phone: str, email: str):
    contact = Contact(name=name, phone=phone, email=email)
    db.add(contact)
    db.commit()
    db.refresh(contact)
    return contact

def get_all_contacts(db: Session):
    return db.query(Contact).all()

def get_contact_by_id(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()

    def update_contact(db: Session, contact_id: int, name: str, phone: str, email: str):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        contact.name = name
        contact.phone = phone
        contact.email = email
        db.commit()
        db.refresh(contact)
    return contact

def delete_contact(db: Session, contact_id: int):
    contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if contact:
        db.delete(contact)
        db.commit()
    return contact

"""
