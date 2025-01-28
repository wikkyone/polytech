import math


def area_and_length(stdin):
    circle_area = round((math.pi * pow(float(stdin), 2)), 2)
    circle_length = round((math.pi * 2 * float(stdin)), 2)
    return f"Circle area = {circle_area}, circle length = {circle_length}"
