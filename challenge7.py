file = open('challenge7.txt', 'r+')
lines = file.readlines()

acc = 0
seen = {}
i = 0
while i in range(len(lines)):
    if seen.get(i):
        break

    seen[i] = True
    i, acc = process(i, lines[i].strip(), acc)

# Answer to Part 1
print(acc)

def process(index, line, acc):
    if line[0:3] == 'nop':
        return index + 1, acc
    elif line[0:3] == 'acc':
        return index + 1, acc + int(line[3:])
    elif line[0:3] == 'jmp':
        return index + int(line[3:]), acc

for j in range(len(lines)):
    copy_lines = lines.copy()
    if 'jmp' in copy_lines[j]:
        copy_lines[j] = copy_lines[j].replace('jmp', 'nop')
    elif 'nop' in copy_lines[j]:
        copy_lines[j] = copy_lines[j].replace('nop', 'jmp')

    seen = {}
    acc = 0
    i = 0
    while i in range(len(lines)):
        if seen.get(i):
            break

        seen[i] = True
        i, acc = process(i, copy_lines[i].strip(), acc)

    if i >= len(lines):
        break

# Answer to Part 2
print(acc)
