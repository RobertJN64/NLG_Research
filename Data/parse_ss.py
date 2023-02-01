key_data = { #F3 is special
    "G7": [2, 2, 2, 2, 1],
    "H1": [2, 1, 2, 2, 1],
    "J2": [2, 2, 1, 2, 2],
    "K5": [1, 1, 2, 1, 1]
}

with open("ss.txt") as f:
    lines = [line.strip().split('\t') for line in f.readlines()]

for line in lines[1:]:
    if line[0] == 'F3':
        print("-1\t-1\t-1\t-1\t-1")
        continue
    data = key_data[line[0]]
    for index, (a, b) in enumerate(zip(data, line[2:])):
        if str(b) == '-1':
            print('-1', end='')
        elif str(a) == str(b):
            print('1', end='')
        else:
            print('0', end='')
        if index == 4:
            print('\n', end='')
        else:
            print('\t', end='')