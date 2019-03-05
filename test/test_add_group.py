# -*- coding: utf-8 -*-
from model.group import Group
import time


def test_add_group(app):
    # Prepare data
    tmstp = str(time.time())
    ind = tmstp[13:16]
    new_group = Group(name="Group" + ind, header="Header" + ind, footer="Footer" + ind)
    old_groups = app.group.get_group_list()
    # Create the group itself
    app.group.create(new_group)
    assert len(old_groups) + 1 == app.group.count()
    # new_groups = sorted(new_groups, key=lambda gr: gr.id)
    new_groups = app.group.get_group_list()
    old_groups.append(new_group)
    # old_groups = sorted(old_groups, key = lambda gr: gr.id)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    empty_group = Group(name="", header="", footer="")
    old_groups = app.group.get_group_list()
    app.group.create(empty_group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(empty_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
