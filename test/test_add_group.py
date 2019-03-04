# -*- coding: utf-8 -*-
from model.group import Group
import time


def test_add_group(app):
     # Prepare data
     tmstp = str(time.time())
     ind = tmstp[13:15]
     new_group = Group(name="Group"+ind, header="Header"+ind, footer="Footer"+ind)
     old_groups = app.group.get_group_list()
     # Create the group itself
     app.group.create(new_group)
     new_groups = app.group.get_group_list()
     assert len(old_groups)+1==len(new_groups)

def test_add_empty_group(app):
    empty_group = Group(name="", header="", footer="")
    old_groups = app.group.get_group_list()
    app.group.create(empty_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


