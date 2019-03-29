from model.group import Group
import random


def test_delete_group(app, db, check_ui):
    # for index in range(1,101):
    if len(db.get_group_list()) == 0:
        app.group.create(Group(name="Group for deletion"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    app.group.delete_by_id(group.id)
    new_groups = db.get_group_list()
    old_groups.remove(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        for i in range(0, len(new_groups)):
            new_groups[i] = new_groups[i].clear()
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
