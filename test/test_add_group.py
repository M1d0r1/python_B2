# -*- coding: utf-8 -*-
from model.group import Group
import pytest
import allure

def test_add_group(app, db, check_ui, json_groups):
    new_group = json_groups
    with allure.step("Get old groups list"):
         old_groups = db.get_group_list()
    with allure.step("When I add a group %s to the list" % new_group):
        app.group.create(new_group)
    with allure.step("Then the new list of groups is equal to the old list with the added group"):
        new_groups = db.get_group_list()
        old_groups.append(new_group.clear())
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            for i in range(0, len(new_groups)):
                new_groups[i] = new_groups[i].clear()
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
