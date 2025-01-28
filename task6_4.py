def Read_file_last(filename, n):
    with open(filename, "r") as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    return lines[-n:]
