# -*- coding: utf-8 -*-
from model.contact import Contact
from utils.formatstrings import FormatStrings


def test_add_contact(app, db, json_contacts):
    new_contact = json_contacts
    old_contacts = db.get_contact_list()
    app.contact.create(new_contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
