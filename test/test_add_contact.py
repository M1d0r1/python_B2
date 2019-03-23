# -*- coding: utf-8 -*-
from model.contact import Contact
from utils.formatstrings import FormatStrings


def test_add_contact(app, json_contacts):
    new_contact = json_contacts
    app.open_start_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(new_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    new_contact.first_name = FormatStrings.clear_spaces(new_contact.first_name)
    new_contact.last_name = FormatStrings.clear_spaces(new_contact.last_name)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
