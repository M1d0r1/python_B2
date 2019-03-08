from model.group import Group
from random import randrange


def test_modify_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group for modification"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = app.group.get_data(index)
    # Prepare data
    group.name = "%s %s" % (group.name, app.data.get_random_string())
    group.header = "%s %s" % (group.header, app.data.get_random_string())
    group.footer = "%s %s" % (group.footer, app.data.get_random_string())
    group.id = old_groups[index].id
    # Modify the group
    app.group.modify_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_modify_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Group for modification"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="Only name" + str(index))
    group.id = old_groups[index].id
    # Modify the group
    app.group.modify_by_index(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
