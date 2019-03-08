import os
import datetime
from model.contact import Contact
from random import randrange


def test_modify_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for modification"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = app.contact.get_data_by_index(index)
    # Prepare data
    contact.first_name = "%s %s" %(contact.first_name, app.data.get_random_string())
    contact.middle_name = "%s %s" % (contact.middle_name, app.data.get_random_string())
    contact.last_name = "%s %s" % (contact.last_name, app.data.get_random_string())
    contact.nickname = "%s %s" % (contact.nickname, app.data.get_random_string())
    dir = os.getcwd()
    if dir[len(dir) - 5:len(dir)] == r"\test":
        contact.photo_keys = dir + r'\Resource\photo2.jpg'
    else:
        contact.photo_keys = dir + r'\test\Resource\photo2.jpg'
    contact.title = "%s %s" % (contact.title, app.data.get_random_string())
    contact.company = "%s %s" % (contact.company, app.data.get_random_string())
    contact.primary_address = "%s\n%s" % (contact.primary_address, app.data.get_random_string())
    if contact.primary_home_phone is not "":
        contact.primary_home_phone = str(int(contact.primary_home_phone) + 1)
    else:
        contact.primary_home_phone = app.data.get_random_phone()
    contact.secondary_address = "%s\n%s" % (contact.secondary_address, app.data.get_random_string())
    if contact.secondary_home_phone is not "":
        contact.secondary_home_phone = str(int(contact.secondary_home_phone) + 1)
    else:
        contact.secondary_home_phone = app.data.get_random_phone()
    if contact.mobile_phone is not "":
        contact.mobile_phone = str(int(contact.mobile_phone) + 1)
    else:
        contact.mobile_phone = app.data.get_random_phone()
    if contact.work_phone is not "":
        contact.work_phone = str(int(contact.work_phone) + 1)
    else:
        contact.work_phone = app.data.get_random_phone()
    if contact.fax is not "":
        contact.fax = str(int(contact.fax) + 1)
    else:
        contact.fax = app.data.get_random_phone()
    contact.email1 = app.data.get_random_string()+ contact.email1
    contact.email2 = app.data.get_random_string() + contact.email2
    contact.email3 = app.data.get_random_string() + contact.email3
    contact.homepage = "%s%s.com" % (contact.homepage[0:11], app.data.get_random_string())
    if contact.birthdate is not None:
        contact.birthdate = datetime.date(contact.birthdate.year + 1, contact.birthdate.month,
                                          (contact.birthdate.day + 1) % 27 + 1)
    if contact.anniversary_date is not None:
        contact.anniversary_date = datetime.date(contact.anniversary_date.year + 1, contact.anniversary_date.month,
                                                 (contact.anniversary_date.day + 1) % 27 + 1)
    contact.notes = "%s\n%s" % (app.data.get_random_multistring(), contact.notes)
    app.open_start_page()
    contact.id = old_contacts[index].id
    # Modify the contact
    app.contact.modify_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


def test_modify_contact_name(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(first_name="Contact for modification"))
    app.open_start_page()
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(first_name="New Contact Name Only "+str(index))
    contact.id = old_contacts[index].id
    contact.last_name = old_contacts[index].last_name
    # Modify the contact
    app.contact.modify_by_index(index, contact)
    assert len(old_contacts) == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
