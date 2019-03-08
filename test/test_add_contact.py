# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact
import datetime
import os


def test_add_contact(app):
    # Prepare data
    birthdate = datetime.date(1980, 11, 20)
    anniversary_date = datetime.date(2005, 3, 14)
    new_group = Group(name="Group " + app.data.get_random_string(), header="Header " + app.data.get_random_string(), footer="Footer " + app.data.get_random_string())
    app.group.create(new_group)
    dir = os.getcwd()
    if dir[len(dir) - 5:len(dir)] == r"\test":
        photo_keys = dir + r'\Resource\photo.jpg'
    else:
        photo_keys = dir + r'\test\Resource\photo.jpg'
    # Create the contact itself
    new_contact = Contact(first_name= "Name "+ app.data.get_random_string(), middle_name="Middle name " + app.data.get_random_string(), last_name="Last name " + app.data.get_random_string(),
                          nickname="Nickname " + app.data.get_random_string(), photo_keys=photo_keys, title="Title " + app.data.get_random_string(),
                          company="Company " + app.data.get_random_string(), primary_address=app.data.get_random_multistring(),
                          primary_home_phone= app.data.get_random_phone(),
                          secondary_address=app.data.get_random_multistring(),
                          secondary_home_phone=app.data.get_random_phone(), mobile_phone=app.data.get_random_phone(),
                          work_phone=app.data.get_random_phone(), fax=app.data.get_random_phone(), email1=app.data.get_random_string() + "@gmail.com",
                          email2=app.data.get_random_string()+ "@mail.ru", email3=app.data.get_random_string() + "@myjob.com",
                          homepage="https://%s.com" % app.data.get_random_string(), birthdate=birthdate,
                          anniversary_date=anniversary_date, group=new_group, notes="here is my note\n"+app.data.get_random_multistring())
    app.open_start_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(new_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
