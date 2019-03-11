import random
import string

class RandomData:

    def __init__(self):
        pass

    def get_random_string(self):
        ind = random.randrange(20)
        return ''.join([random.choice(string.ascii_letters + string.digits+""*10) for i in range(ind)])

    def get_random_phone(self):
        return str(random.randrange(1000000,9999999))

    def get_random_multistring(self):
        return "%s\n%s\n%s" % (self.get_random_string(), self.get_random_string(), self.get_random_string())