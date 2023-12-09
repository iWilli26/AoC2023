import math
import re

file1 = open("./day8/input.txt", "r")
lines = file1.readlines()
file1.close()
    
directions = lines[0] 

map = {}
positions = []
for line in lines[2:]:
    temp = line.split("=") 
    location = temp[0][:-1]
    if location[2] == "A":
        positions.append(location)
    leftRight = temp[1].replace("\n","")[2:-1].split(", ")
    map[location] = {
        "left" : leftRight[0],
        "right" : leftRight[1],
    }

sum = 0
win = True
while win:
    for i in range(len(directions)):
        win = False
        for i in range(len(positions)):
            if directions[i] == "R":
                positions[i] = map[positions[i]]["right"]
                sum += 1
            elif directions[i] == "L":
                positions[i] = map[positions[i]]["left"]
                sum += 1                
            if i == len(directions) - 1:
                i=0
            if positions[i][2] != "Z":
                win =True
        print(positions)
                
print(sum)