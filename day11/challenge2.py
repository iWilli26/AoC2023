import networkx as nx
import math

file1 = open("./day11/input.txt", "r")
lines = file1.readlines()
file1.close()

def visualizeUniverse():
    galaxyString = ""
    for line in universe:
        for char in line:
            galaxyString += char
        galaxyString += "\n"
    print(galaxyString)

universe = []
for line in lines:
    universe.append(list(line.strip()))

emptyLines = []
for i in range(len(universe)):
    if universe[i].count(".") == len(universe[i]):
        emptyLines.append(i)

emptyColumns = []
for i in range(len(universe[0])):
    column = []
    for j in range(len(universe)):
        column.append(universe[j][i])
    if column.count(".") == len(column):
        emptyColumns.append(i)

# counter= 0
# for empty in emptyLines:
#     universe.insert(empty+counter, ["."]*len(universe[0]))
#     counter += 1

# counter = 0
# for empty in emptyColumns:
#     for i in range(len(universe)):
#         universe[i].insert(empty+counter, ".")
#     counter += 1

galaxies = []
for y in range(len(universe)):
    for x in range(len(universe[y])):
        if universe[y][x] == "#":
            galaxies.append((x, y))

f = open("./day11/coupleGalaxies.txt", "r")
lines = f.readlines()
f.close()

if(len(lines) > 0):
    galaxyPairs = eval(lines[0])
else:
    galaxyPairs = []
    for i in range(len(galaxies)):
        for j in range(len(galaxies)):
            if i != j and (galaxies[j], galaxies[i]) not in galaxyPairs:
                galaxyPairs.append((galaxies[i], galaxies[j]))
    f = open("./day11/coupleGalaxies.txt", "a")
    f.write(str(galaxyPairs))
    f.close()

sum=0
for pair in galaxyPairs:
    for ok in emptyLines:
        if (ok > pair[0][1] and ok < pair[1][1]) or (ok > pair[1][1] and ok < pair[0][1]):
            sum += 1000000 -1
    for ok in emptyColumns:
        if (ok > pair[0][0] and ok < pair[1][0]) or (ok > pair[1][0] and ok < pair[0][0]):
            sum += 1000000 -1
            
    distance =abs(pair[0][0]-pair[1][0]) + abs(pair[0][1]-pair[1][1])
    
    sum += distance
print(sum)
