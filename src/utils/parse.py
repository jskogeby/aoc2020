def inp(input_file, form=int):
    with open(input_file, "r") as file:
        return [form(r.strip()) for r in file.readlines()]

def split_input(input_file, split_char="\n"):
    with open(input_file, "r") as file:
        data = file.read().strip()
        data =  data.split(split_char)
        return data

def split_lines(lines, split_char, form):
    testForm = len(lines[0].split(split_char)) == len(form)
    if not testForm:
        print("Input split does not match form")
        exit(1)
    output = []
    for line in lines:
        splits = [form[i](split) for i, split in enumerate(line.split(split_char))]
        output.append(splits)
    return output

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
