from __future__ import print_function

field = []

for x in range(0, 10):
    field.append([])

for x in range(0, 10):
    for y in range(0, 10):
        if x == 0 or y == 0 or x == 9 or y == 9:
            field[x].append('#')
        else:
            field[x].append(' ')

for x in range(0, 10):
    for y in range(0, 10):
        print(field[x][y], end='')
    print('\n', end='')
