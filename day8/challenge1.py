import math
import re

file1 = open("./day8/input.txt", "r")
lines = file1.readlines()
file1.close()
    
directions = lines[0] 

map = {}

for line in lines[2:]:
    temp = line.split("=") 
    location = temp[0][:-1]
    leftRight = temp[1].replace("\n","")[2:-1].split(", ")
    map[location] = {
        "left" : leftRight[0],
        "right" : leftRight[1],
    }

position = "AAA"
sum = 0
while position != "ZZZ":
    for i in range(len(directions)):
        if directions[i] == "R":
            position = map[position]["right"]
            sum += 1
        elif directions[i] == "L":
            position = map[position]["left"]
            sum += 1
        if position == "ZZZ":
            break
        if i == len(directions) - 1:
            i=0
print(sum)