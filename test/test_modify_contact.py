import datetime
import random
from model.contact import Contact
from utils.formatstrings import FormatStrings
from utils.randomdata import RandomData


def test_modify_contact(app, db):
    if len(db.get_contact_list()) == 0:
        app.contact.create(Contact(first_name="Contact for deletion"))
    old_contacts = db.get_contact_list()
    old_contact = random.choice(old_contacts)
    # Prepare data
    contact = Contact()
    contact.first_name = "%s %s" % (old_contact.first_name, RandomData.get_random_string())
    contact.middle_name = "%s %s" % (old_contact.middle_name, RandomData.get_random_string())
    contact.last_name = "%s %s" % (old_contact.last_name, RandomData.get_random_string())
    contact.nickname = "%s %s" % (old_contact.nickname, RandomData.get_random_string())
    contact.title = "%s %s" % (old_contact.title, RandomData.get_random_string())
    contact.company = "%s %s" % (old_contact.company, RandomData.get_random_string())
    contact.primary_address = "%s\n%s" % (old_contact.primary_address, RandomData.get_random_string())
    if old_contact.primary_home_phone is not "":
        contact.primary_home_phone = str(int(old_contact.primary_home_phone) + 1)
    else:
        contact.primary_home_phone = RandomData.get_random_phone()
    contact.secondary_address = "%s\n%s" % (old_contact.secondary_address, RandomData.get_random_string())
    if old_contact.secondary_home_phone is not "":
        contact.secondary_home_phone = str(int(old_contact.secondary_home_phone) + 1)
    else:
        contact.secondary_home_phone = RandomData.get_random_phone()
    if old_contact.mobile_phone is not "":
        contact.mobile_phone = str(int(old_contact.mobile_phone) + 1)
    else:
        contact.mobile_phone = RandomData.get_random_phone()
    if old_contact.work_phone is not "":
        contact.work_phone = str(int(old_contact.work_phone) + 1)
    else:
        contact.work_phone = RandomData.get_random_phone()
    if old_contact.fax is not "":
        contact.fax = str(int(old_contact.fax) + 1)
    else:
        contact.fax = RandomData.get_random_phone()
    contact.email1 = RandomData.get_random_string() + old_contact.email1
    contact.email2 = RandomData.get_random_string() + old_contact.email2
    contact.email3 = RandomData.get_random_string() + old_contact.email3
    contact.homepage = "%s%s.com" % (old_contact.homepage[0:11], RandomData.get_random_string())
    if old_contact.birthdate is not None:
        contact.birthdate = datetime.date(old_contact.birthdate.year + 1, old_contact.birthdate.month,
                                          (old_contact.birthdate.day + 1) % 27 + 1)
    if old_contact.anniversary_date is not None:
        contact.anniversary_date = datetime.date(old_contact.anniversary_date.year + 1, old_contact.anniversary_date.month,
                                                 (old_contact.anniversary_date.day + 1) % 27 + 1)
    contact.notes = "%s\n%s" % (RandomData.get_random_multistring(), old_contact.notes)
    app.open_start_page()
    contact.id = old_contact.id
    # Modify the contact
    app.contact.modify_by_id(contact.id, contact)
    new_contacts = app.contact.get_contact_list()
    old_contacts.remove(old_contact)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_modify_contact_name(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(first_name="Contact for modification"))
#     app.open_start_page()
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     contact = Contact(first_name="New Contact Name Only " + str(index))
#     contact.id = old_contacts[index].id
#     contact.last_name = old_contacts[index].last_name
#     # Modify the contact
#     app.contact.modify_by_index(index, contact)
#     assert len(old_contacts) == app.contact.count()
#     new_contacts = app.contact.get_contact_list()
#     contact.first_name = FormatStrings.clear_spaces(contact.first_name)
#     contact.last_name = FormatStrings.clear_spaces(contact.last_name)
#     old_contacts[index] = contact
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
