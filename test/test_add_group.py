# -*- coding: utf-8 -*-
from model.group import Group


def test_add_group(app):
    # Prepare data
    new_group = Group(name="Group " + app.data.get_random_string(), header="Header " + app.data.get_random_string(), footer="Footer " + app.data.get_random_string())
    old_groups = app.group.get_group_list()
    # Create the group itself
    app.group.create(new_group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    empty_group = Group(name="", header="", footer="")
    old_groups = app.group.get_group_list()
    app.group.create(empty_group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(empty_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
