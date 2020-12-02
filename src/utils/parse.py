def inp(input_file, format=int):
    with open(input_file, "r") as file:
        return [format(r.strip()) for r in file.readlines()]
