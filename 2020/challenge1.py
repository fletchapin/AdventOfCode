import pandas as pd
import numpy as np

entries = pd.read_csv('data/2020/challenge1.txt', sep=' ', header=None)
valid_count = 0

for i in range(0, entries[0].size):
    entry = entries.iloc[i]
    requirement_min, requirement_max = entry[0].split("-")
    letter = entry[1][0]
    count = 0
    for character in entry[2]:
        if letter == character:
            count += 1

    if count >= int(requirement_min) and count <= int(requirement_max):
        valid_count += 1

# Answer to Part 1
print(valid_count)

valid_count = 0
for i in range(0, entries[0].size):
    entry = entries.iloc[i]
    first_char, second_char = entry[0].split("-")
    first_char_idx = int(first_char) - 1
    second_char_idx = int(second_char) - 1
    letter = entry[1][0]
    bool1 = entry[2][first_char_idx] == letter
    bool2 = entry[2][second_char_idx] == letter

    if (bool1 and not bool2) or (bool2 and not bool1):
        valid_count += 1

# Answer to Part 2
print(valid_count)
