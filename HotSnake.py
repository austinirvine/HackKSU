from __future__ import print_function

def grow_snake(snk, dir):
    if dir == 1:
        snk.insert(0, [snk[0][0]-1, snk[0][1]])
    elif dir == 2:
        snk.insert(0, [snk[0][0], snk[0][1]+1])
    elif dir == 3:
        snk.insert(0, [snk[0][0]+1, snk[0][1]])
    elif dir == 4:
        snk.insert(0, [snk[0][0], snk[0][1]-1])

    return(snk)

def move_snake(snk, dir):
    if dir == 1:
        snk.insert(0, [snk[0][0]-1, snk[0][1]])
    elif dir == 2:
        snk.insert(0, [snk[0][0], snk[0][1]+1])
    elif dir == 3:
        snk.insert(0, [snk[0][0]+1, snk[0][1]])
    elif dir == 4:
        snk.insert(0, [snk[0][0], snk[0][1]-1])

    del snk[len(snk) - 1]

    return(snk)

def update_field(fld, size, snk):
    for x in range(0, size):
        for y in range(0, size):
            if x == 0 or y == 0 or x == size - 1 or y == size - 1:
                field[x][y] = "#"
            else:
                field[x][y] = " "

    for x in range(0, len(snk)):
        fld[snk[x][0]][snk[x][1]] = "X"

    return(fld)

def draw_field(fld):
    for x in fld:
        for y in x:
            print(y, end='')
        print('\n', end='')

def is_game_over(fld, snk):
    for x in range(0, size):
        for y in range(0, size):
            if (x == 0 or y == 0 or x == size - 1 or y == size - 1) and fld[x][y] != "#":
                return True

    for x in range(0, len(snk)):
        for y in range(0, len(snk)):
            if [[snk[x][0]],[snk[x][1]]] == [[snk[y][0]],[snk[y][1]]] and x != y:
                return True

    return False

#variables
field = []
snake = []
size = 20
direction = 3

#create initial snake
snake.append([int(size / 2), int(size / 2)])

#create initial field
for x in range(0, size):
    field.append([])

for x in range(0, size):
    for y in range(0, size):
        if x == 0 or y == 0 or x == size - 1 or y == size - 1:
            field[x].append("#")
        else:
            field[x].append(" ")

while is_game_over(field, snake) == False:
    field = update_field(field, size, snake)
    draw_field(field)

    if is_game_over(field, snake) == False:
        direction = int(input(": "))

        snake = grow_snake(snake, direction)
