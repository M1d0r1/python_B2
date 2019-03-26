from model.contact import Contact
import random


def test_delete_contact(app, db):
    # for i in range (0,200):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Contact for deletion"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    old_contacts.remove(contact)
    new_contacts = db.get_contact_list()
    print("old ",old_contacts,"new ", new_contacts)
    assert old_contacts == new_contacts
