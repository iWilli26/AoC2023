import math
import re

file1 = open("./day10/input.txt", "r")
lines = file1.readlines()
file1.close()

def getAroundTiles(x:int, y:int):
    aroundTiles = []
    try:
        aroundTiles.append(world[y-1][x])
    except:
        pass
    try:
        aroundTiles.append(world[y+1][x])
    except:
        pass
    try:
        aroundTiles.append(world[y][x-1])
    except:
        pass
    try:
        aroundTiles.append(world[y][x+1])
    except:
        pass
    if x-1<0:
        aroundTiles.remove(world[y][x-1])
    if y-1<0:
        aroundTiles.remove(world[y-1][x])
    return aroundTiles

def isPath(x:int, y:int):
    if world[y][x+1] == "-" or world[y][x+1] == "J" or world[y][x+1] == "7":
        return True, (x+1, y)
    elif world[y][x-1] == "-" or world[y][x-1] == "F" or world[y][x-1] == "L":
        return True, (x-1, y)
    elif world[y+1][x] == "|" or world[y+1][x] == "F" or world[y+1][x] == "7":
        return True, (x, y+1)
    elif world[y-1][x] == "|" or world[y-1][x] == "J" or world[y-1][x] == "L":
        return True, (x, y-1)
    else:
        return False
    

world = []
for line in lines:
    line = line.strip()
    line = line.replace("\n", "")
    world.append(list(line))

for y in range(len(world)):
    for x in range(len(world[y])):
        if world[y][x] == "S":
            startX = x
            startY = y

for tile in getAroundTiles(startX, startY):
    print(isPath(startX, startY))