# -*- coding: utf-8 -*-
from model.group import Group
import pytest
from test.randomdata import RandomData

rand = RandomData()

testdata = [
Group(name=name, header=header, footer=footer)
for name in ["", "Name"+rand.get_random_string()]
for header in ["", "Header"+rand.get_random_string()]
for footer in ["", "Footer"+rand.get_random_string()]
]

@pytest.mark.parametrize("new_group", testdata, ids=[repr(x) for x in testdata])
def test_add_group(app,new_group):
    # Prepare data
    old_groups = app.group.get_group_list()
    # Create the group itself
    app.group.create(new_group)
    assert len(old_groups) + 1 == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups.append(new_group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



