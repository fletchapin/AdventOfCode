def prep_binary(val, mask_len):
    binary_rep = bin(int(val))[2:]
    i = mask_len - len(binary_rep)
    prepend = ''
    if i > 0:
        for j in range(0, i):
            prepend = prepend + '0'

    return prepend + binary_rep

def process_part_1(mask, instructions, mem):
    for instruction in instructions:
        idx, _, val = instruction.split(" ")
        idx = idx[4:len(idx) - 1]

        mem[idx] = apply_mask_part_1(val, mask)

    return mem

def apply_mask_part_1(val, mask):
    binary_rep = prep_binary(val, len(mask))

    for j in range(0, len(mask)):
        if mask[j] == 'X':
            continue
        elif mask[j] != binary_rep[j]:
            binary_rep = binary_rep[:j] + mask[j] + binary_rep[j + 1:]

    return int(binary_rep, 2)

def process_part_2(mask, instructions, mem):
    for instruction in instructions:
        idx, _, val = instruction.split(" ")
        idx = idx[4:len(idx) - 1]
        binary_rep = prep_binary(idx, len(mask))
        possible_idx = apply_mask_part_2(binary_rep, mask, indices=[])

        for i in possible_idx:
            mem[i] = int(val)

    return mem

def apply_mask_part_2(binary_rep, mask, indices=[], lower_bound=0):
    for j in range(lower_bound, len(mask)):
        if mask[j] == '0':
            continue
        elif mask[j] == '1':
            binary_rep = binary_rep[:j] + '1' + binary_rep[j + 1:]
        elif mask[j] == 'X':
            indices = apply_mask_part_2(
                binary_rep[:j] + '0' + binary_rep[j + 1:],
                mask,
                indices=indices,
                lower_bound=j + 1,
            )
            indices = apply_mask_part_2(
                binary_rep[:j] + '1' + binary_rep[j + 1:],
                mask,
                indices=indices,
                lower_bound=j + 1,
            )
            return indices

    indices.append(int(binary_rep, 2))
    return indices

def run(filepath):
    file = open(filepath, 'r+')
    lines = [line.strip() for line in file.readlines()]

    data = {}
    mask = None
    instructions = []
    for line in lines:
        if line[0:4] == "mask":
            if mask:
                data[mask] = instructions
                instructions = []
            mask = line.strip()[7:]
        else:
            instructions.append(line.strip())

    data[mask] = instructions

    mem = {}
    for mask, instructions in data.items():
        mem = process_part_1(mask, instructions, mem)

    # Answer to Part 1
    print(sum(mem.values()))

    mem = {}
    for mask, instructions in data.items():
        mem = process_part_2(mask, instructions, mem)
        # print(mem)

    # Answer to Part 2
    print(sum(mem.values()))

run('data/2020/challenge13.txt')

# Test for Part 1
assert apply_mask_part_1('11', 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X') == 73
run('data/2020/challenge13_test0.txt')

# Test for Part 2
assert apply_mask_part_2('000000000000000000000000000000101010', '000000000000000000000000000000X1001X', indices=[]) == [26, 27, 58, 59]
assert apply_mask_part_2('000000000000000000000000000000011010', '00000000000000000000000000000000X0XX', indices=[]) == [16, 17, 18, 19, 24, 25, 26, 27]
run('data/2020/challenge13_test1.txt')
