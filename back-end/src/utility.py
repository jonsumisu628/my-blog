import random
import string


def random_string(length):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(length)])
