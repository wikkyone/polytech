import random


def random_integer(stdin1, stdin2):
    first = int(stdin1)
    second = int(stdin2)
    result = random.randint(first, second)
    return result
