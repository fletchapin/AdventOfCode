import numpy as np
import math

def lcm(a, b=None):
    if isinstance(a, (list, np.ndarray, tuple)):
        if b is None:
            if len(a) > 1:
                return lcm(a[1:], a[0])
            else:
                return a[0]
        elif len(a) == 1:
            return lcm(a[0], b)
        else:
            return lcm(lcm(a[1:], a[0]), b)
    else:
        return a * b // math.gcd(a, b)

file = open('challenge12.txt', 'r+')
lines = [line.strip() for line in file.readlines()]

start = int(lines[0])
bus_ids = [int(id) for id in lines[1].split(',') if id != 'x']
departure_times = [start + id - start % id for id in bus_ids]

# Answer to Part 1
print((min(departure_times) - start)
      * bus_ids[departure_times.index(min(departure_times))])

required_diff = [i % int(id) for i, id in enumerate(lines[1].split(',')) if id != 'x']

index = np.array(np.argsort(bus_ids), dtype='int64')
sorted_ids = np.array(np.flip([bus_ids[idx] for idx in index]), dtype='int64')
sorted_diff = np.flip([required_diff[idx] for idx in index])
least_common_multiples = [lcm(sorted_ids[0:j]) for j in range(1, len(sorted_ids))]
least_common_multiples.insert(0, 1)

i = 100000000000342
success = False
while not success:
    success = True
    for j, id in enumerate(sorted_ids):
        if i % id != sorted_diff[j]:
            sum = least_common_multiples[j]
            i += sum
            success = False
            break

    if i > 10000000000000000:
        break

# Answer to Part 2
print(i)
