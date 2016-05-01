from __future__ import print_function
import random
import api

#grows the snake one forward
def grow_snake(snk, dir):
    if dir == "w":
        snk.insert(0, [snk[0][0]-1, snk[0][1]])
    elif dir == "d":
        snk.insert(0, [snk[0][0], snk[0][1]+1])
    elif dir == "s":
        snk.insert(0, [snk[0][0]+1, snk[0][1]])
    elif dir == "a":
        snk.insert(0, [snk[0][0], snk[0][1]-1])

    return(snk)

#deletes the last block of the snake
def remove_snake_tail(snk, dir):
    del snk[len(snk) - 1]
    return(snk)

#update the state of the game field
def update_field(fld, size, snk, orb_loc):
    for x in range(0, size):
        for y in range(0, size):
            if x == 0 or y == 0 or x == size - 1 or y == size - 1:
                field[x][y] = "#"
            else:
                field[x][y] = " "

    for x in range(0, len(snk)):
        fld[snk[x][0]][snk[x][1]] = "X"

    #to see the orb, uncomment the following line
    #fld[orb_loc[0]][orb_loc[1]] = "O"

    return(fld)

#draw the game field to the screen
def draw_field(fld):
    for x in fld:
        for y in x:
            print(y, end='')
        print('\n', end='')

#checks to see if the game is over (player hits wall or themself)
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

#creates a new orb
def create_orb(fld, size):
    random.seed()
    temp1 = random.randint(1, size-2)
    temp2 = random.randint(1, size-2)
    while (fld[temp1][temp2] != " "):
        temp1 = random.randint(1, size-2)
        temp2 = random.randint(1, size-2)

    orb_loc = [temp1, temp2]

    return orb_loc

#checks to see if the snake has landed on the orb
def snake_is_on_orb(orb_loc, snk):
    if [snk[0][0],snk[0][1]] == orb_loc:
        update_light("green", 1)
        return True
    else:
        return False

#returns the distance from the snake's head to the orb
def distance_to_orb(orb_loc, snk):
    return(abs(orb_loc[0]-snk[0][0]) + abs(orb_loc[1] - snk[0][1]))

def update_light(color, bright):
    payload = {
        "color": color,
        "brightness": bright,
    }
    api.put(payload)

################################################################################

#variables
field = []
snake = []
size = 20
direction = 3
orb = []
temp = 0
color = "white"
bright = 1

payload = {
    "power": "on",
}
api.put(payload)

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
temp = distance_to_orb(orb, snake)
update_light(color, bright)

#the game loop; runs until game over is reached
while is_game_over(field, snake) == False:
    field = update_field(field, size, snake, orb)
    draw_field(field)

    #checks to see if the game is over to run this part of code
    if is_game_over(field, snake) == False:
        #DELETE THE LINE BELOW
        #print(distance_to_orb(orb, snake))

        #gather user input
        direction = str(input(": "))

        #check to see if the snake has landed on the orb
        if snake_is_on_orb(orb, grow_snake(snake, direction)) == True:
            color = "green"
            orb = create_orb(field, size)
            temp = distance_to_orb(orb, snake)
        else:
            snake = remove_snake_tail(snake, direction)

            if(distance_to_orb(orb, snake) < temp):
                if(color == "red"):
                    bright+=0.1
                    update_light(color, bright)
                    temp = distance_to_orb(orb, snake)
                else:
                    color = "red"
                    bright = 0.1
                    update_light(color, bright)
                    temp = distance_to_orb(orb, snake)
            else:
                if(color == "blue"):
                    bright+=0.1
                    update_light(color, bright)
                    temp = distance_to_orb(orb, snake)
                else:
                    color = "blue"
                    bright = 0.1
                    update_light(color, bright)
                    temp = distance_to_orb(orb, snake)
#game over screen with score
bright = 1
color = "orange"
update_light(color, bright)
color = "green"
update_light(color, bright)
color = "purple"
update_light(color, bright)
color = "white"
update_light(color, bright)
payload = {
    "power": "off",
}
api.put(payload)
print("\n\n")
print("-----------------------------------------")
print("               -Game Over-\n")
print("\t\tScore:\t" + str(len(snake)))
print("-----------------------------------------")
