# Assignment 8: TileTraveller
# jonra20, rutt20, valurg20
# Github: https://github.com/Jon-Robert/TileTraveller

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

def orr(direction):
    if len(direction) > 1:
        return direction + " or "
    else:
        return ""

def movement(x,y,direction):

    if direction == "N" or direction == "n":
        y+=1
    elif direction == "E" or direction == "e":
        x+=1
    elif direction == "S" or direction == "s":
        y-=1
    elif direction == "W" or direction == "w":
        x-=1
        
    return (x,y)
 
xHnit = 1
yHnit = 1


while not (xHnit == 3 and yHnit == 1):
    travel = ""
    check_location = location(xHnit,yHnit)
    #do the function stuffs
    
    if "n" in check_location:
        travel = orr(travel)
        travel += "(N)orth"
    if "e" in check_location:
        travel = orr(travel)
        travel += "(E)ast"
    if "s" in check_location:
        travel = orr(travel)
        travel += "(S)outh"
    if "w" in check_location:
        travel = orr(travel)
        travel += "(W)est"
   
    print("You can travel:",travel+'.')
    direction = input("Direction: ")
    if direction in check_location:
        (xHnit,yHnit) = movement(xHnit,yHnit,direction)
    else:
        print("Not a valid direction!")

print("Victory!")