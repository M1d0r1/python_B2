from model.group import Group
import random
import allure

def test_delete_group(app, db, check_ui):
    with allure.step("If there are no groups create one"):
        if len(db.get_group_list()) == 0:
            app.group.create(Group(name="Group for deletion"))
    with allure.step("Given list of groups"):
        old_groups = db.get_group_list()
    with allure.step("When deleting a group"):
        group = random.choice(old_groups)
        app.group.delete_by_id(group.id)
    with allure.step("Then a new list of groups is equal to the old list with a deleted group"):
        new_groups = db.get_group_list()
        old_groups.remove(group)
        assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
        if check_ui:
            for i in range(0, len(new_groups)):
                new_groups[i] = new_groups[i].clear()
            assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)
