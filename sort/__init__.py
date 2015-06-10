import random


def random_list(n):
    random_list = list(range(n))
    random.shuffle(random_list)
    return random_list