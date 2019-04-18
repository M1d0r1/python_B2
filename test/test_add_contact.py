# -*- coding: utf-8 -*-
from model.contact import Contact
import allure

def test_add_contact(app, db, json_contacts, check_ui):
    new_contact = json_contacts
    with allure.step("Given old contact list"):
        old_contacts = db.get_contact_list()
    with allure.step("When I add a new contact"):
        app.contact.create(new_contact)
    with allure.step("Then the new list of contacts is equal to the old list with the added contact"):
        new_contacts = db.get_contact_list()
        old_contacts.append(new_contact)
        assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
        if check_ui:
            for i in range(0, len(new_contacts)):
                new_contacts[i] = new_contacts[i].clear()
            assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)
