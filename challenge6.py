file = open('challenge6.txt', 'r+')
lines = file.readlines()

bag_dict = {}
for line in lines:
    bag_list = line.strip().split('bags')
    key = bag_list.pop(0).strip()
    values = {}
    for bag in bag_list:
        if bag in ['.', ',', '', ' ']:
            pass
        elif 'bag' in bag:
            bag_list1 = bag.split('bag')
            for subbag in bag_list1:
                if subbag != '.':
                    bag_name, bag_num = parse_bag(subbag)
                    values[bag_name] = bag_num
        else:
            bag_name, bag_num = parse_bag(bag)
            values[bag_name] = bag_num

    bag_dict[key] = values

answers_dict = {}
for bag_name in list(bag_dict.keys()):
    answers_dict = solve(bag_name, bag_dict, answers_dict)

sum = 0
for _, value in answers_dict.items():
    if value:
        sum += 1

print(sum)
print(russian_doll('shiny gold', bag_dict) - 1)

def russian_doll(bag_name, bag_dict):
    sum = 1
    for bag, bag_num in bag_dict[bag_name].items():
        if bag is not None:
            sum += bag_num * russian_doll(bag, bag_dict)
        else:
            return 1

    return sum

def parse_bag(bag):
    if ' contain ' in bag:
        bag = bag.replace(' contain ', '')
    elif ',' in bag:
        bag = bag.replace(',', '')
    elif '.' in bag:
        bag = bag.replace('.', '')

    if bag.strip() == 'no other' or bag == '':
        return None, None
    else:
        bag_num = bag.strip().split(' ')[0]
        bag_name = bag.replace(bag_num, '').strip()
        return bag_name, int(bag_num)

def solve(bag_name, bag_dict, prev_answers):
    try:
        _ = prev_answers[bag_name]
    except KeyError:
        prev_answers[bag_name] = False
        for bag, _ in bag_dict[bag_name].items():
            if bag == 'shiny gold':
                prev_answers[bag_name] = True
            elif bag is not None:
                prev_answers = solve(bag, bag_dict, prev_answers)
                if prev_answers[bag]:
                    prev_answers[bag_name] = True

    return prev_answers
