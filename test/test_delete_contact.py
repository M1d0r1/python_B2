from model.contact import Contact
import random
from time import sleep


def test_delete_contact(app, db, check_ui):
    # for i in range (0,200):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Contact for deletion"))
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    app.contact.delete_by_id(contact.id)
    old_contacts.remove(contact)
    sleep(1)
    new_contacts = db.get_contact_list()
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        for i in range(0, len(new_contacts)):
            new_contacts[i] = new_contacts[i].clear()
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
