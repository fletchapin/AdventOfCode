import numpy as np

file = open('data/2020/challenge10.txt', 'r+')
lines = file.readlines()

matrix = []
for line in lines:
    row = [character for character in line.strip()]
    matrix.append(row)

attempts = 0
start = []
while np.any(start != matrix):
    start = np.array(matrix).copy()
    matrix = process(matrix, start)
    attempts += 1

count = 0
for row in matrix:
    for char in row:
        if char == '#':
            count += 1

# Answer to Part 1
print(count)

matrix = []
for line in lines:
    row = [character for character in line.strip()]
    matrix.append(row)

attempts = 0
start = []
while np.any(start != matrix):
    start = np.array(matrix).copy()
    matrix = process(matrix, start, line_of_sight=True)
    attempts += 1

count = 0
for row in matrix:
    for char in row:
        if char == '#':
            count += 1

# Answer to Part 2
print(count)

def process(matrix, orig_matrix, line_of_sight=False):
    for j, row in enumerate(matrix):
        for i, char in enumerate(row):
            if char == '.':
                continue
            else:
                if line_of_sight:
                    row[i] = process_line_of_sight((j, i), char, orig_matrix)
                else:
                    row[i] = process_adjacent((j, i), char, orig_matrix)

    return matrix

def process_adjacent(index, character, matrix):
    adjacent_idx = [(index[0] - 1, index[1] - 1), (index[0], index[1] - 1),
                    (index[0] + 1, index[1] - 1), (index[0] + 1, index[1]),
                    (index[0] + 1, index[1] + 1), (index[0] - 1, index[1]),
                    (index[0] - 1, index[1] + 1), (index[0], index[1] + 1)]
    if character == 'L':
        no_occupied = True
        for idx in adjacent_idx:
            if idx[0] < 0 or idx[1] < 0:
                continue
            try:
                if matrix[idx[0]][idx[1]] == '#':
                    no_occupied = False
            except IndexError:
                pass
        if no_occupied:
            return '#'
    elif character == '#':
        occupied_count = 0
        for idx in adjacent_idx:
            if idx[0] < 0 or idx[1] < 0:
                continue
            try:
                if matrix[idx[0]][idx[1]] == '#':
                    occupied_count += 1
            except IndexError:
                pass
        if occupied_count >= 4:
            return 'L'

    return character

def process_line_of_sight(index, character, matrix):
    adjacent_idx = [(index[0] - 1, index[1] - 1), (index[0], index[1] - 1),
                    (index[0] + 1, index[1] - 1), (index[0] + 1, index[1]),
                    (index[0] + 1, index[1] + 1), (index[0] - 1, index[1]),
                    (index[0] - 1, index[1] + 1), (index[0], index[1] + 1)]
    if character == 'L':
        no_occupied = True
        for idx in adjacent_idx:
            while (idx[0] < len(matrix) and idx[1] < len(matrix[idx[0]])
                   and idx[0] >= 0 and idx[1] >= 0
                   and matrix[idx[0]][idx[1]] == '.'):
                idx = move_direction(idx, index)
            if idx[0] < 0 or idx[1] < 0:
                continue
            try:
                if matrix[idx[0]][idx[1]] == '#':
                    no_occupied = False
            except IndexError:
                pass
        if no_occupied:
            return '#'
    elif character == '#':
        occupied_count = 0
        for idx in adjacent_idx:
            while (idx[0] < len(matrix) and idx[1] < len(matrix[idx[0]])
                   and idx[0] >= 0 and idx[1] >= 0
                   and matrix[idx[0]][idx[1]] == '.'):
                idx = move_direction(idx, index)
            if idx[0] < 0 or idx[1] < 0:
                continue
            try:
                if matrix[idx[0]][idx[1]] == '#':
                    occupied_count += 1
            except IndexError:
                pass
        if occupied_count >= 5:
            return 'L'

    return character

def move_direction(index, orig_index):
    new_index = []
    for i in [0, 1]:
        if index[i] < orig_index[i]:
            new_index.append(index[i] - 1)
        elif index[i] > orig_index[i]:
            new_index.append(index[i] + 1)
        else:
            new_index.append(index[i])

    return new_index
