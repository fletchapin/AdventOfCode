import numpy as np

file = open('challenge4.txt', 'r+')
lines = file.readlines()

ids = []
max_id = 0
for line in lines:
    id = get_id(line.rstrip())
    ids.append(id)

    if id > max_id:
        max_id = id

print(max_id)

ids = np.sort(ids)
prev = ids[0]
for i in range(1, len(ids)):
    if ids[i] - 1 != prev:
        print(ids[i] - 1)
        # ids[i:] -= 8

    prev = ids[i]
    
def get_id(string):
    row = parse(string[0:7], True)
    col = parse(string[7:], False)
    return row * 8 + col

def parse(string, is_row):
    if is_row:
        max_possible = 127
    else:
        max_possible = 7
    min_possible = 0
    for character in string:
        if character == 'F' or character == 'L':
            max_possible = (max_possible + min_possible - 1) / 2
        if character == 'B' or character == 'R':
            min_possible = (max_possible + min_possible + 1) / 2

    return min_possible
