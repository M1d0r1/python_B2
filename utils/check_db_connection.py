from fixture.orm import ORMFixture

orm = ORMFixture(host="localhost", name="addressbook", user="root",password="")

try:
    l = orm.get_contact_list()
    #l = orm.get_group_list()
    for item in l:
        print(item)
    print(len(l))
finally:
    pass