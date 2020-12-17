import numpy as np

file = open('challenge3.txt', 'r+')
lines = file.readlines()

passports = []
info = ''
for line in lines:
    if line == '\n':
        passports.append(info.rstrip())
        info = ''
    else:
        info = info + line.rstrip() + ' '

info = info + line.rstrip() + ' '
passports.append(info.rstrip())

def is_valid(name, value):
    if name == 'byr':
        try:
            result = int(value) >= 1920 and int(value) <= 2002
        except:
            result = False

    elif name == 'iyr':
        try:
            result = int(value) >= 2010 and int(value) <= 2020
        except:
            result = False

    elif name == 'eyr':
        try:
            result = int(value) >= 2020 and int(value) <= 2030
        except:
            result = False

    elif name == 'hgt':
        # try:
        if value[-2:] == 'in':
            result = int(value[0:-2]) >= 59 and int(value[0:-2]) <= 76

        elif value[-2:] == 'cm':
            result = int(value[0:-2]) >= 150 and int(value[0:-2]) <= 193

        else:
            result = False
        # except:
        #     result = False
    elif name == 'hcl':
        if value[0] == '#':
            result = True
            for character in value[1:]:
                if character not in ['0', '1', '2', '3', '4', '5', '6', '7',
                                     '8', '9', 'a', 'b', 'c', 'd', 'e', 'f']:
                    result = False
        else:
            result = False

    elif name == 'ecl':
        acceptable = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        result = value in acceptable

    elif name == 'pid':
        result = len(value) == 9 and value.isdigit()

    else:
        result = True

    return result

count = 0
for pp in passports:
    required = {'byr': False, 'iyr': False, 'eyr': False, 'hgt': False,
                'hcl': False, 'ecl': False, 'pid': False}
    fields = pp.split(' ')
    for field in fields:
        field = field.split(':')
        name = field[0]
        value = field[1]
        required[name] = is_valid(name, value)

    if np.all(list(required.values())):
        count += 1

# Answer to Part 1 overwritten
# Answer to Part 2
print(count)
