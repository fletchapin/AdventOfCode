input = [13, 16, 0, 12, 15, 1]
answers = {13: 0, 16: 1, 0: 2, 12: 3, 15: 4}

def solve(input, answers, limit=2020):
    for i in range(len(input) - 1, limit - 1):
        if input[i] in list(answers.keys()):
            input.append(i - answers[input[i]])
        else:
            input.append(0)
        answers[input[i]] = i

    return input[-1]

# Answer to Part 1
print(solve(input, answers))

# Answer to Part 2
print(solve(input, answers, limit=30000000))

# Test for Part 1
assert solve([1, 3, 2], {1: 0, 3: 1}) == 1
assert solve([0, 3, 6], {0: 0, 3: 1}) == 436
