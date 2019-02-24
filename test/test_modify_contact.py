import os
import datetime
from model.contact import Contact

def test_modify_first_contact(app):
    contact = app.contact.get_data_first()
    #Prepare data
    contact.first_name = contact.first_name + " upd"
    contact.middle_name = contact.middle_name + "upd"
    contact.last_name = contact.last_name + " upd"
    contact.nickname = contact.nickname + " upd"
    dir = os.getcwd()
    if dir[len(dir) - 5:len(dir)] == r"\test":
        contact.photo_keys = dir + r'\Resource\photo2.jpg'
    else:
        contact.photo_keys = dir + r'\test\Resource\photo2.jpg'
    contact.title = contact.title + " upd"
    contact.company = contact.company + " upd"
    contact.primary_address = contact.primary_address + " upd"
    contact.primary_home_phone = str(int(contact.primary_home_phone) + 1)
    contact.secondary_address = contact.secondary_address + " upd"
    contact.secondary_home_phone = str(int(contact.secondary_home_phone) + 1)
    contact.mobile_phone = str(int(contact.mobile_phone) + 1)
    contact.work_phone = str(int(contact.work_phone) + 1)
    contact.fax = str(int(contact.fax) + 1)
    contact.email1 = "upd" + contact.email1
    contact.email2 = "upd" + contact.email2
    contact.email3 = "upd" + contact.email3
    contact.homepage = contact.homepage[0:11] + "upd.com"
    contact.birthdate = datetime.date(contact.birthdate.year + 1, contact.birthdate.month,
                                      (contact.birthdate.day + 1) % 27+1)
    contact.anniversary_date = datetime.date(contact.anniversary_date.year + 1, contact.anniversary_date.month,
                                             (contact.anniversary_date.day + 1) % 27+1)
    contact.notes = "Update\n" + contact.notes
    # Modify the contact
    app.contact.modify_first(contact)

def test_modify_first_contact_name(app):
    app.contact.modify_first(Contact(first_name="New Contact Name Only"))
