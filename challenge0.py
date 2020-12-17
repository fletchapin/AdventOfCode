import pandas as pd
import numpy as np

entries = pd.read_csv('challenge0.csv', header=None)
entries.sort_values(0, inplace=True, ignore_index=True)

for i in range(entries.size - 1, 0, -1):
    entry = entries.at[i, 0]
    result =  entry + entries
    if (result == 2020).any()[0]:
        answer = np.where(result == 2020)[0][0]
        break

# Answer to Part 1
print("The answer is " + str(entries.at[i, 0] * entries.at[answer, 0]))

for j in range(entries.size - 1, 0, -1):
    entry0 = entries.at[j, 0]
    for i in range(entries.size - 1, 0, -1):
        entry1 = entries.at[i, 0]
        result = entry0 + entry1 + entries
        if (result == 2020).any()[0]:
            answer = np.where(result == 2020)[0][0]
            break
    if (result == 2020).any()[0]:
        answer = np.where(result == 2020)[0][0]
        break

# Answer to Part 2
print("The answer is " + str(entries.at[i, 0] * entries.at[j, 0] * entries.at[answer, 0]))
