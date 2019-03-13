def test_clear_groups(app):
    for i in range(0, app.group.count()):
        app.group.delete_by_index(0)


def test_clear_contacts(app):
    for i in range(0, app.contact.count()):
        app.contact.delete_by_index(0)
        app.open_start_page()
        app.wd.find_element_by_link_text("add new")
