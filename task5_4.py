import math


def discriminant_root(stdin):
    stdin_split = stdin.split()
    discriminant = pow(float(stdin_split[1]), 2) - 4 * float(stdin_split[0]) * float(
        stdin_split[2]
    )
    if discriminant < 0:
        return "Дискриминант меньше нуля"
    else:
        return math.sqrt(discriminant)
