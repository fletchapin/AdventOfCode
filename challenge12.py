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


def get_valid(possible, ids, diff):
    result = None
    for i in range(0, len(possible)):
        t0 = possible[i]
        try:
            for j in range(0, len(ids)):
                t = t0 + diff[j]
                assert t % ids[j] == 0

            result = possible[i]
            break
        except AssertionError:
            pass

    return result

def process(ids, diff, lcm_list, sum=1, i=1, possible=[], limit=10000000):
    success = False
    while not success:
        if i > limit:
            break
        success = True
        last = None
        for j, id in enumerate(ids):
            if last is None:
                if i % id == diff[j]:
                    last = True
                    continue
                elif i % id == id - diff[j]:
                    last = False
                    continue
                elif lcm_list[j] > sum:
                    possible = process(ids, diff, lcm_list,
                                       lcm_list[j], i=lcm_list[j] - i,
                                       possible=possible)
                    possible = process(ids, diff, lcm_list,
                                       lcm_list[j], i=lcm_list[j] + i,
                                       possible=possible)

                    if j < len(ids) - 1 and i > 2 * lcm_list[j]:
                        return possible
                    else:
                        sum = lcm_list[j]

                i += sum
                success = False
                break

            elif (i % id == diff[j] and not last):
                last = True
                continue
            elif (i % id == id - diff[j] and last):
                last = False
                continue
            else:
                if lcm_list[j] > sum:
                    possible = process(ids, diff, lcm_list,
                                       lcm_list[j], i=lcm_list[j] - i,
                                       possible=possible)
                    possible = process(ids, diff, lcm_list,
                                       lcm_list[j], i=lcm_list[j] + i,
                                       possible=possible)

                    if j < len(ids) - 1 and i > 2 * lcm_list[j]:
                        return possible
                    else:
                        sum = lcm_list[j]

                i += sum
                success = False
                break

        if success:
            possible.append(i)

    return possible

def run(filepath, i=1, limit=10000000):
    file = open(filepath, 'r+')
    lines = [line.strip() for line in file.readlines()]

    start = int(lines[0])
    bus_ids = [int(id) for id in lines[1].split(',') if id != 'x']
    departure_times = [start + id - start % id for id in bus_ids]

    # Answer to Part 1
    print((min(departure_times) - start)
          * bus_ids[departure_times.index(min(departure_times))])

    required_diff = [i % int(id) for i, id in enumerate(lines[1].split(',')) if id != 'x']

    start = int(lines[0])
    bus_ids = [int(id) for id in lines[1].split(',') if id != 'x']
    departure_times = [start + id - start % id for id in bus_ids]

    index = np.array(np.argsort(bus_ids), dtype='int64')
    sorted_ids = np.array(np.flip([bus_ids[idx] for idx in index]), dtype='int64')
    sorted_diff = np.flip([required_diff[idx] for idx in index])
    least_common_multiples = [lcm(sorted_ids[0:j]) for j in range(1, len(sorted_ids))]
    least_common_multiples.insert(0, 1)

    possible = process(sorted_ids, sorted_diff, least_common_multiples, sum=1,
                       i=i, limit=limit)
    possible.sort()
    print(possible)

    # Answer to Part 2
    print(get_valid(list(set(possible)), bus_ids, required_diff))

run('challenge12_test0.txt')
run('challenge12_test1.txt')
run('challenge12_test2.txt')
run('challenge12_test3.txt')
run('challenge12.txt', limit=10000000000000000)
