# -*- coding: utf-8 -*-
from model.group import Group
import time


def test_add_group(app):
     app.session.login(admin="admin", password="secret")
     # Prepare data
     tmstp = str(time.time())
     ind = tmstp[13:15]
     new_group = Group(name="Group"+ind, header="Header"+ind, footer="Footer"+ind)
     # Create the group itself
     app.group.create(new_group)
     app.session.logout()



def test_add_empty_group(app):
    app.session.login(admin="admin", password="secret")
    empty_group = Group(name="", header="", footer="")
    app.group.create(empty_group)
    app.session.logout()

