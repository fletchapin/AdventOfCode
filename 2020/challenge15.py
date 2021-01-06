def run(filepath):
    file = open(filepath, 'r+')
    lines = [line.strip() for line in file.readlines()]

run('data/2020/challenge15.txt')
