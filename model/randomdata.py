import random
import string

class RandomData:

    def __init__(self):
        pass

    @staticmethod
    def get_random_string():
        ind = random.randrange(20)
        return ''.join([random.choice(string.ascii_letters + string.digits+" "*10) for i in range(ind)])

    @staticmethod
    def get_random_phone():
        return str(random.randrange(1000000,9999999))

    @staticmethod
    def get_random_multistring():
        return "%s\n%s\n%s" % (RandomData.get_random_string(), RandomData.get_random_string(), RandomData.get_random_string())