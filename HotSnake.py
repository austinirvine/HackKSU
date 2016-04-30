from __future__ import print_function

field = []
size = 20

for x in range(0, size):
    field.append([])

for x in range(0, size):
    for y in range(0, size):
        if x == 0 or y == 0 or x == size - 1 or y == size - 1:
            field[x].append('#')
        else:
            field[x].append(' ')

for x in range(0, size):
    for y in range(0, size):
        print(field[x][y], end='')
    print('\n', end='')
