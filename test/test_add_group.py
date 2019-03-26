# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app, db, check_ui, json_groups):
    new_group = json_groups
    old_groups = db.get_group_list()
    app.group.create(new_group)
    new_groups = db.get_group_list()
    old_groups.append(new_group.clear())
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        for i in range(0, len(new_groups)):
            new_groups[i] = new_groups[i].clear()
        assert sorted(new_groups, key = Group.id_or_max) == sorted(app.group.get_group_list(), key = Group.id_or_max)
