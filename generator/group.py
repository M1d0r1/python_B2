from model.group import Group
from utils.randomdata import RandomData
import os.path
import json

testdata = [Group(name="Name" + RandomData.get_random_string(),header="Header" + RandomData.get_random_string(), footer = "Footer" + RandomData.get_random_string())
            for i in range(5)
            ]+[Group(name="",footer="", header="")]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/groups.json")

with open(file, "w") as f:
    f.write(json.dumps(testdata, default=lambda x: x.__dict__))