"""import unittest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base, Contact
from app.crud import create_contact, get_all_contacts, get_contact_by_id, update_contact, delete_contact

class TestContactMethods(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        DATABASE_URL = "sqlite:///./test.db"
        cls.engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
        Base.metadata.create_all(bind=cls.engine)
        cls.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=cls.engine)

    @classmethod
    def tearDownClass(cls):
        Base.metadata.drop_all(bind=cls.engine)
        cls.engine.dispose()

    def setUp(self):
        self.db = self.SessionLocal()

    def tearDown(self):
        self.db.close()

    def test_create_contact(self):
        contact = create_contact(self.db, "Test Contact", "000-000-0000", "test@example.com")
        self.assertEqual(contact.name, "Test Contact")
        self.assertEqual(contact.phone, "000-000-0000")
        self.assertEqual(contact.email, "test@example.com")

    def test_get_all_contacts(self):
        create_contact(self.db, "Contact 1", "111-111-1111", "contact1@example.com")
        create_contact(self.db, "Contact 2", "222-222-2222", "contact2@example.com")
        contacts = get_all_contacts(self.db)
        self.assertEqual(len(contacts), 2)

    def test_get_contact_by_id(self):
        contact = create_contact(self.db, "Contact 3", "333-333-3333", "contact3@example.com")
        retrieved_contact = get_contact_by_id(self.db, contact.id)
        self.assertEqual(retrieved_contact.name, "Contact 3")

    def test_update_contact(self):
        contact = create_contact(self.db, "Contact 4", "444-444-4444", "contact4@example.com")
        updated_contact = update_contact(self.db, contact.id, "Updated Contact", "555-555-5555", "updated@example.com")
        self.assertEqual(updated_contact.name, "Updated Contact")
        self.assertEqual(updated_contact.phone, "555-555-5555")
        self.assertEqual(updated_contact.email, "updated@example.com")

    def test_delete_contact(self):
        contact = create_contact(self.db, "Contact 5", "555-555-5555", "contact5@example.com")
        delete_contact(self.db, contact.id)
        deleted_contact = get_contact_by_id(self.db, contact.id)
        self.assertIsNone(deleted_contact)

if __name__ == "__main__":
    unittest.main()"""
