file = open('challenge5.txt', 'r+')
lines = file.readlines()

forms = []
answers = ''
for line in lines:
    if line == '\n':
        forms.append(answers)
        answers = ''
    else:
        answers = answers + line.rstrip()

answers = answers + line.rstrip()
forms.append(answers.rstrip())

sum = 0
for answer in forms:
    sum += len(set(answer))

print(sum)

forms = []
answers = []
for line in lines:
    if line == '\n':
        forms.append(answers)
        answers = []
    else:
        answers.append(line.rstrip())

answers.append(line.rstrip())
forms.append(answers)

sum = 0
for answers in forms:
    if len(answers) == 1:
        sum += len(set(answers[0]))
    else:
        for letter in set(answers[0]):
            valid = True
            for i in range(1, len(answers)):
                if letter not in answers[i]:
                    valid = False
                    break

            if valid:
                sum += 1

print(sum)
