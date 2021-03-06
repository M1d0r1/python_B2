from model.group import Group
from utils.randomdata import RandomData
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:],"n:f:",["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/groups.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

testdata = [Group(name="Name" + RandomData.get_random_string(),header="Header" + RandomData.get_random_string(), footer = "Footer" + RandomData.get_random_string())
            for i in range(n-1)
            ]+[Group(name="",footer="", header="")]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)),  "..", f)

with open(file, "w") as out_file:
    jsonpickle.set_encoder_options("json", indent = 2)
    out_file.write(jsonpickle.encode(testdata))