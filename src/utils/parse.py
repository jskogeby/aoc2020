def inp(input_file, form=int):
    with open(input_file, "r") as file:
        return [form(r.strip()) for r in file.readlines()]

def split_input(input_file, split_char, subsplit_char=None, form=(str, str)):
    with open(input_file, "r") as file:
        data = file.read()
        data =  data.split(split_char)
        if subsplit_char:
            data = [subsplit.split(subsplit_char) for subsplit in data]
        return data

# If data should be grouped between blank lines
def group(data):
    groups = []
    curr = []
    for d in data:
        if not d:
            groups.append(curr)
            curr = []
        else:
            curr.append(d)
    groups.append(curr)
    return groups

def unpack(data):
    return [item for sublist in data for item in sublist]

    