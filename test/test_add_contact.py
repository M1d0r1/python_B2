# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact
import time
import datetime

def test_add_contact(app):
    app.session.login("admin", "secret")
    # Set the index in order to distinguish the created groups and contacts
    tmstp = str(time.time())
    ind = tmstp[13:15]
    # Set contact dates
    birthdate = datetime.date(1980, 11, 20)
    anniversary_date = datetime.date(2005, 3, 14)
    # Create a group for the contact
    group = Group(name="Group" + ind, header="Header" + ind,footer="Footer" + ind)
    app.group.create(group)
    # Create the contact itself
    contact = Contact(first_name="Name"+ind, middle_name="Middle name"+ind, last_name="Last name"+ind, nickname="Nickname"+ind, title = "Title"+ind, company = "Company"+ind, primary_address="Country\nCity\nStreet,"+tmstp[13], primary_home_phone = tmstp[4:7]+tmstp[13:16], secondary_address="Country\nCity\nStreet,"+tmstp[15], secondary_home_phone=tmstp[3:6] + tmstp[14:17], mobile_phone = tmstp[0:8], work_phone = tmstp[1:9],fax = tmstp[2:10],email1=tmstp[0:5]+"@gmail.com", email2=tmstp[6:10]+"@mail.ru", email3=tmstp[8:11]+"@myjob.com",homepage = "https://"+tmstp[13:20]+".com", birthdate = birthdate, anniversary_date = anniversary_date, group = group, notes="here is my note")
    app.contact.create(contact)
    app.session.logout()



