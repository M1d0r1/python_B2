from model.contact import Contact
import random
from time import sleep
import allure

def test_delete_contact(app, db, check_ui):
    with allure.step("If there are no contacts create one"):
        if len(db.get_contact_list()) == 0:
            app.contact.create(Contact(first_name="Contact for deletion"))
    with allure.step("Given list of contacts"):
        old_contacts = db.get_contact_list()
    with allure.step("When delete a contact"):
        contact = random.choice(old_contacts)
        app.contact.delete_by_id(contact.id)
    with allure.step("Then a new list of contacts is equal to old list with a deleted contact"):
        old_contacts.remove(contact)
        sleep(1)
        new_contacts = db.get_contact_list()
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            for i in range(0, len(new_contacts)):
                new_contacts[i] = new_contacts[i].clear()
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)
