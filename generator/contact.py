from model.contact import Contact
from utils.randomdata import RandomData
import os.path
import jsonpickle
import getopt
import sys
import datetime

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 2
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a

birthdate = datetime.date(1980, 11, 20)
anniversary_date = datetime.date(2005, 3, 14)
photo_keys = os.path.dirname(os.path.abspath(__file__)) + "\\resource\\photo.jpg"
# photo_keys = os.path.join(os.path.dirname(os.path.abspath(__file__)), "/resource/photo.jpg")

testdata = [
               (Contact(first_name="Name" + RandomData.get_random_string(),
                        middle_name="Middle name" + RandomData.get_random_string(),
                        last_name="Last name" + RandomData.get_random_string(),
                        nickname="Nickname" + RandomData.get_random_string(),
                        photo_keys=photo_keys, title="Title " + RandomData.get_random_string(),
                        company="Company " + RandomData.get_random_string(),
                        primary_address=RandomData.get_random_multistring(),
                        primary_home_phone=RandomData.get_random_phone(),
                        secondary_address=RandomData.get_random_multistring(),
                        secondary_home_phone=RandomData.get_random_phone(), mobile_phone=RandomData.get_random_phone(),
                        work_phone=RandomData.get_random_phone(), fax=RandomData.get_random_phone(),
                        email1=RandomData.get_random_string() + "@gmail.com",
                        email2=RandomData.get_random_string() + "@mail.ru",
                        email3=RandomData.get_random_string() + "@myjob.com",
                        homepage="https://%s.com" % RandomData.get_random_string(), birthdate=birthdate,
                        anniversary_date=anniversary_date,
                        notes="here is my note\n" + RandomData.get_random_multistring()))
               for i in range(n-1)
           ] + [Contact(first_name=" ")]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out_file:
    jsonpickle.set_encoder_options("json", indent=2)
    out_file.write(jsonpickle.encode(testdata))
