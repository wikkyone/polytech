def read_file(filename):
    with open(filename, "r") as file:
        lines = file.readlines()
    lines = [line.strip() for line in lines]
    return lines
