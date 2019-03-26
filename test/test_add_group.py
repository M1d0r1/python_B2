# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, json_groups):
    new_group = json_groups
    old_groups = db.get_group_list()
    app.group.create(new_group)
    new_groups = db.get_group_list()
    old_groups.append(new_group.clear())
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
