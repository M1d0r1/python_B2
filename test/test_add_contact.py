# -*- coding: utf-8 -*-
from model.contact import Contact
import datetime
import os
from utils.randomdata import RandomData
import pytest
from utils.formatstrings import FormatStrings

birthdate = datetime.date(1980, 11, 20)
anniversary_date = datetime.date(2005, 3, 14)
dir = os.getcwd()
if dir[len(dir) - 5:len(dir)] == r"\test":
     photo_keys = dir + r'\Resource\photo.jpg'
else:
     photo_keys = dir + r'\test\Resource\photo.jpg'


testdata = [
(Contact(first_name="Name"+RandomData.get_random_string(), middle_name="Middle name"+RandomData.get_random_string(),
        last_name="Last name"+RandomData.get_random_string(), nickname="Nickname"+RandomData.get_random_string(),
        photo_keys=photo_keys,title="Title " + RandomData.get_random_string(),
        company="Company " + RandomData.get_random_string(),
        primary_address=RandomData.get_random_multistring(),
        primary_home_phone=RandomData.get_random_phone(),
        secondary_address=RandomData.get_random_multistring(),
        secondary_home_phone=RandomData.get_random_phone(), mobile_phone=RandomData.get_random_phone(),
        work_phone=RandomData.get_random_phone(), fax = RandomData.get_random_phone(),
        email1=RandomData.get_random_string() + "@gmail.com",
        email2=RandomData.get_random_string() + "@mail.ru",
        email3=RandomData.get_random_string() + "@myjob.com",
        homepage="https://%s.com" % RandomData.get_random_string(), birthdate=birthdate,
        anniversary_date=anniversary_date,
        notes="here is my note\n" + RandomData.get_random_multistring()))
        for i in range(5)
     ]+[Contact(first_name=" ")]

@pytest.mark.parametrize("new_contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, new_contact):
    app.open_start_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(new_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    new_contact.first_name = FormatStrings.clear_spaces(new_contact.first_name)
    new_contact.last_name = FormatStrings.clear_spaces(new_contact.last_name)
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
