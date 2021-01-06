input = [13, 16, 0, 12, 15, 1]
answers = {13: 0, 16: 1, 0: 2, 12: 3, 15: 4}

def solve(input, answers, limit=2020):
    next = input[len(input) - 1]
    for i in range(len(input) - 1, limit):
        prev = next
        if answers.get(prev) is not None:
            next = i - answers[prev]
        else:
            next = 0
        answers[prev] = i

    return prev

# Answer to Part 1
print(solve(input, answers))

# reset values since answers was modified
input = [13, 16, 0, 12, 15, 1]
answers = {13: 0, 16: 1, 0: 2, 12: 3, 15: 4}

# Answer to Part 2
print(solve(input, answers, limit=30000000))

# Test for Part 1
assert solve([1, 3, 2], {1: 0, 3: 1}) == 1
assert solve([0, 3, 6], {0: 0, 3: 1}) == 436

def main():
    print(solve(input, answers, limit=300000))
