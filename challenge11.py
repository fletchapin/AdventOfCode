file = open('challenge11.txt', 'r+')
lines = [line.strip() for line in file.readlines()]

pos = (0, 0, 0)
for line in lines:
    pos = move_part_1(line, pos)

# Answer to Part 1
print(abs(pos[0]) + abs(pos[1]))

def move_part_1(instruction, position):
    if instruction[0] == 'F':
        if position[2] == 0:
            return (position[0], position[1] + int(instruction[1:]), position[2])
        if position[2] == 180:
            return (position[0], position[1] - int(instruction[1:]), position[2])
        if position[2] == 270:
            return (position[0] + int(instruction[1:]), position[1], position[2])
        if position[2] == 90:
            return (position[0] - int(instruction[1:]), position[1], position[2])
    elif instruction[0] == 'E':
        return (position[0], position[1] + int(instruction[1:]), position[2])
    elif instruction[0] == 'W':
        return (position[0], position[1] - int(instruction[1:]), position[2])
    elif instruction[0] == 'N':
        return (position[0] + int(instruction[1:]), position[1], position[2])
    elif instruction[0] == 'S':
        return (position[0] - int(instruction[1:]), position[1], position[2])
    elif instruction[0] == 'R' or instruction[0] == 'L':
        return (position[0], position[1], transform(position[2], instruction))

def transform(start_dir, instruction):
    if instruction[0] == 'R':
        new_dir = start_dir + int(instruction[1:])
        return new_dir - 360 if new_dir >= 360 else new_dir
    elif instruction[0] == 'L':
        new_dir = start_dir - int(instruction[1:])
        return new_dir + 360 if new_dir < 0 else new_dir

ship_pos = (0, 0)
way_pos = (10, 1)
i = 0
for line in lines:
    (ship_pos, way_pos) = move_part_2(line, ship_pos, way_pos)

# Answer to Part 2
print(abs(ship_pos[0]) + abs(ship_pos[1]))

def move_part_2(instruction, ship_position, waypoint):
    if instruction[0] == 'F':
        return (
                   (
                       ship_position[0] + waypoint[0] * int(instruction[1:]),
                       ship_position[1] + waypoint[1] * int(instruction[1:]),
                   ),
                   waypoint
        )
    elif instruction[0] == 'N':
        return ((ship_position[0], ship_position[1]),
                (waypoint[0], waypoint[1] + int(instruction[1:])))
    elif instruction[0] == 'S':
        return ((ship_position[0], ship_position[1]),
                (waypoint[0], waypoint[1] - int(instruction[1:])))
    elif instruction[0] == 'W':
        return ((ship_position[0], ship_position[1]),
                (waypoint[0] - int(instruction[1:]), waypoint[1]))
    elif instruction[0] == 'E':
        return ((ship_position[0], ship_position[1]),
                (waypoint[0] + int(instruction[1:]), waypoint[1]))
    elif instruction[0] == 'R' or instruction[0] == 'L':
        return ((ship_position[0], ship_position[1]),
                rotate((waypoint[0], waypoint[1]), instruction))

def rotate(waypoint, instruction):
    degrees = int(instruction[1:])
    if degrees == 180:
            return -waypoint[0], -waypoint[1]
    elif (instruction[0] == 'R' and degrees == 90):
        return waypoint[1], -waypoint[0]
    elif (instruction[0] == 'R' and degrees == 270):
        return rotate((waypoint[1], -waypoint[0]), 'R180')
    elif (instruction[0] == 'L' and degrees == 90):
        return -waypoint[1], waypoint[0]
    elif (instruction[0] == 'L' and degrees == 270):
        return rotate((-waypoint[1], waypoint[0]), 'L180')
