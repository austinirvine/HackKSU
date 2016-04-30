from __future__ import print_function

#def grow_snake(snek):

def move_snake(snek, dir):
    snek.insert(0, [snek+1, snek])
    del snek[len(snek) - 1]

    return(snek)

def update_field(fld, size, snk):
    for x in range(0, size):
        for y in range(0, size):
            if x == 0 or y == 0 or x == size - 1 or y == size - 1:
                field[x].append("#")
            else:
                field[x].append(" ")

    for x in range(0, len(snk)):
        field[snk[x][0]][snk[x][1]] = "X"

field = []
snake = []
size = 20

for x in range(0, size):
    field.append([])

snake.append([int(size / 2), int(size / 2)])

field = update_field(field, size, snake)

for x in range(0, size):
    for y in range(0, size):
        print(str(field[x][y]), end='')
    print('\n', end='')
