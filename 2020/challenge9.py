import pandas as pd

entries = pd.read_csv('data/2020/challenge9.txt', sep=' ', header=None)
entries.sort_values(0, inplace=True, ignore_index=True)

one_count = 0
three_count = 0
for i in range(0, entries.size - 1):
    diff = entries.at[i+1, 0] - entries.at[i, 0]
    if diff == 1:
        one_count += 1
    if diff == 3:
        three_count += 1

# this accounts for wall-to-charger and charger-to-device differences
three_count += 1
one_count += 1

# Answer to Part 1
print(one_count * three_count)

permutations = {}
permutations[entries.at[entries.size - 1, 0]] = 1
for i in range(entries.size - 2, 0, -1):
    entry = entries.at[i, 0]
    permutations[entry] = (
        get_zero_if_none(permutations, entry+1)
        + get_zero_if_none(permutations, entry+2)
        + get_zero_if_none(permutations, entry+3)
    )

permutations[1] = (
    get_zero_if_none(permutations, 2)
    + get_zero_if_none(permutations, 3)
    + get_zero_if_none(permutations, 4)
)

# Answer to Part 2
print(permutations[1] + permutations[2] + permutations[3])

def get_zero_if_none(dict, key):
    try:
        result = dict[key]
    except KeyError:
        result = 0
    return result
