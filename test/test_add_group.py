# -*- coding: utf-8 -*-
from model.group import Group
import time


def test_add_group(app):
     # Prepare data
     tmstp = str(time.time())
     ind = tmstp[13:15]
     new_group = Group(name="Group"+ind, header="Header"+ind, footer="Footer"+ind)
     # Create the group itself
     app.group.create(new_group)


def test_add_empty_group(app):
    empty_group = Group(name="", header="", footer="")
    app.group.create(empty_group)


