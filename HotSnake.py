from __future__ import print_function
import random

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

def remove_snake_tail(snk, dir):
    del snk[len(snk) - 1]
    return(snk)

def update_field(fld, size, snk, orb_loc):
    for x in range(0, size):
        for y in range(0, size):
            if x == 0 or y == 0 or x == size - 1 or y == size - 1:
                field[x][y] = "#"
            else:
                field[x][y] = " "

    for x in range(0, len(snk)):
        fld[snk[x][0]][snk[x][1]] = "X"

    fld[orb_loc[0]][orb_loc[1]] = "O"

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

def create_orb(fld, size):
    random.seed()
    temp1 = random.randint(1, size-2)
    temp2 = random.randint(1, size-2)
    while (fld[temp1][temp2] != " "):
        temp1 = random.randint(1, size-2)
        temp2 = random.randint(1, size-2)

    orb_loc = [temp1, temp2]

    return orb_loc

def snake_is_on_orb(orb_loc, snk):
    if [snk[0][0],snk[0][1]] == orb_loc:
        return True
    else:
        return False

def distance_to_orb(orb_loc, snk):
    return(abs(orb_loc[0]-snk[0][0]) + abs(orb_loc[1] - snk[0][1]))

################################################################################

#variables
field = []
snake = []
size = 20
direction = 3
orb = []

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

#create initial orb
orb = create_orb(field, size)
field = update_field(field, size, snake, orb)

while is_game_over(field, snake) == False:
    field = update_field(field, size, snake, orb)
    draw_field(field)

    if is_game_over(field, snake) == False:
        direction = int(input(": "))

        if snake_is_on_orb(orb, grow_snake(snake, direction)) == True:
            orb = create_orb(field, size)
        else:
            snake = remove_snake_tail(snake, direction)

print("\n\n")
print("-----------------------------------------")
print("               -Game Over-\n")
print("\t\tScore:\t" + str(len(snake)))
print("-----------------------------------------")
