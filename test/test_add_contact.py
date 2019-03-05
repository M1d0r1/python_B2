# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact
import time
import datetime
import os


def test_add_contact(app):
    # Prepare data
    tmstp = str(time.time())
    ind = tmstp[13:16]
    birthdate = datetime.date(1980, 11, 20)
    anniversary_date = datetime.date(2005, 3, 14)
    new_group = Group(name="Group" + ind, header="Header" + ind, footer="Footer" + ind)
    app.group.create(new_group)
    dir = os.getcwd()
    if dir[len(dir) - 5:len(dir)] == r"\test":
        photo_keys = dir + r'\Resource\photo.jpg'
    else:
        photo_keys = dir + r'\test\Resource\photo.jpg'
    # Create the contact itself
    new_contact = Contact(first_name="Name" + ind, middle_name="Middle name" + ind, last_name="Last name" + ind,
                          nickname="Nickname" + ind, photo_keys=photo_keys, title="Title" + ind,
                          company="Company" + ind, primary_address="Country\nCity\nStreet," + tmstp[13],
                          primary_home_phone=tmstp[4:7] + tmstp[13:16],
                          secondary_address="Country\nCity\nStreet," + tmstp[15],
                          secondary_home_phone=tmstp[3:6] + tmstp[14:17], mobile_phone=tmstp[0:8],
                          work_phone=tmstp[1:9], fax=tmstp[2:10], email1=tmstp[0:5] + "@gmail.com",
                          email2=tmstp[6:10] + "@mail.ru", email3=tmstp[8:11] + "@myjob.com",
                          homepage="https://" + tmstp[13:20] + ".com", birthdate=birthdate,
                          anniversary_date=anniversary_date, group=new_group, notes="here is my note")
    app.open_start_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(new_contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(new_contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
