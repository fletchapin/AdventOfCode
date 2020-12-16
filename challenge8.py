file = open('challenge8.txt', 'r+')
lines = file.readlines()

nums = []
for line in lines:
    if len(nums) > 25:
        del nums[0]
    elif len(nums) < 25:
        nums.append(int(line.strip()))
        continue

    val = int(line.strip())
    if not check_sums(val, nums):
        break
    else:
        nums.append(val)

print(val)

def check_sums(val, nums):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == val:
                return True
    return False

goal = 88311122
for i in range(len(lines)):
    sum = int(lines[i].strip())
    cont_nums = [sum]
    for j in range(i+1, len(lines)):
        if sum >= goal:
            break
        else:
            cont_nums.append(int(lines[j].strip()))
            sum += int(lines[j].strip())

    if sum == goal:
        break

print(min(cont_nums) + max(cont_nums))
