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
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    # new_groups = sorted(new_groups, key=lambda gr: gr.id)
    old_groups.append(new_group)
    # old_groups = sorted(old_groups, key = lambda gr: gr.id)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    empty_group = Group(name="", header="", footer="")
    old_groups = app.group.get_group_list()
    app.group.create(empty_group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(empty_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
