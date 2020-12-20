file = open('challenge2.txt', 'r+')
lines = file.readlines()

matrix = []
for line in lines:
    row = []
    for character in line:
        if character == '.':
            row.append(False)
        if character == '#':
            row.append(True)
    matrix.append(row)

def counter(increment0, increment1):
    count = 0
    index = [0, 0]
    while index[1] < len(matrix):
        if index[0] >= len(matrix[0]):
            index[0] -= len(matrix[0])

        if matrix[index[1]][index[0]]:
            count += 1

        index[0] += increment0
        index[1] += increment1

    return count

# Answer to Part 1
print(counter(3, 1))
# Answer to Part 2
print(counter(1, 1) * counter(3, 1) *  counter(5, 1) *  counter(7, 1) *  counter(1, 2))
