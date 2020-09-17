# Assignment 8: TileTraveller
# jonra20, rutt20, valurg20

# print('You can travel: ')

def location(x,y):
    if y == 1:
        return "Nn"
    elif y == 2:
        if x == 1:
            return "NnEeSs"
        elif x == 2:
            return "SsWw"
        elif x == 3:
            return "NnSs"
    elif y == 3:
        if x == 1:
            return "EeSs"
        elif x == 2:
            return "EeWw"
        elif x == 3:
            return "SsWw"

def movement(x,y,direction):

    if direction == "N" or direction == "n":
        y+=1
    elif direction == "E" or direction == "e":
        x+=1
    elif direction == "S" or direction == "s":
        y-=1
    elif direction == "W" or direction == "w":
        x-=1
        
    return x,y
 


xHnit = 1
yHnit = 1


while xHnit != 3 and yHnit != 1:
    #do the function stuffs



