#Algorithm
#x and y axis 
#N and S are + and - on y-axis
#E and W are + and - on x-axis
#Constant immitations so you can't go through certain points
#ask for player direction input
#when x-axis is 3 and y-axis is 1. Program prints victory and stops running
#https://github.com/HBreki/TileTraveller/blob/master/tile_traveller.py

string = ""
x_axis = 1
y_axis = 1
check = True
north = "(N)orth"
south = "(S)outh"
east = "(E)ast"
west = "(W)est"

while True:
    if y_axis == 1:
        change = north + "."
        string = "n"
    if x_axis == 1 and y_axis == 2:
        change = north + " or " + east + " or " + south + "."
        string = "nes"
    if x_axis == 2 and y_axis == 2:
        change = south + " or " + west + "."
        string = "sw"
    if x_axis == 1 and y_axis == 3:
        change = east + " or " + south + "."
        string = "es"
    if x_axis == 2 and y_axis == 3:
        change = east + " or " + west + "."
        string = "we"
    if x_axis == 3 and y_axis == 3:
        change = south + " or " + west + "."
        string = "sw"
    if x_axis == 3 and y_axis == 2:
        change = north + " or " + south + "."
        string = "sn"
    
    if check == True:
        print("You can travel: " + change)
    check = False
    direct = str(input("Direction: "))
    low = direct.lower()

    for l in string:
        if low == l:
            check = True
    
    if check == False:
        print("Not a valid direction!")   

    if check == True:
        if low == "n":
            y_axis += 1
        if low == "s":
            y_axis -= 1
        if low == "e":
            x_axis += 1
        if low == "w":
            x_axis -= 1
    if x_axis == 3 and y_axis == 1:
        break

print("Victory!")