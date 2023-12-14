import math

file1 = open("./day14/input.txt", "r")
lines = file1.readlines()
file1.close()

platform = []
for i in range(len(lines)):    
    platform.append(lines[i].strip())

listO = []    
for y in range(len(platform)):
    for x in range(len(platform[y])):
        if platform[y][x] == "O":
            listO.append((y,x))
def moveUp(y,x,i):
    if y==0 or platform[y-1][x] == "O" or platform[y-1][x] == "#":
        return
    listO[i] = [y-1,x]
    platform[y] = platform[y][:x] + "." + platform[y][x+1:]  
    platform[y-1] = platform[y-1][:x] + "O" + platform[y-1][x+1:]

def moveDown(y,x,i):
    if y==len(platform)-1 or platform[y+1][x] == "O" or platform[y+1][x] == "#":
        return
    listO[i] = [y+1,x]
    platform[y] = platform[y][:x] + "." + platform[y][x+1:]  
    platform[y+1] = platform[y+1][:x] + "O" + platform[y+1][x+1:]

def moveLeft(y,x,i):
    if x==0 or platform[y][x-1] == "O" or platform[y][x-1] == "#":
        return
    listO[i] = [y,x-1]
    platform[y] = platform[y][:x] + "." + platform[y][x+1:]  
    platform[y] = platform[y][:x-1] + "O" + platform[y][x:]

def moveRight(y,x,i):
    if x==len(platform[y])-1 or platform[y][x+1] == "O" or platform[y][x+1] == "#":
        return
    listO[i] = [y,x+1]
    platform[y] = platform[y][:x] + "." + platform[y][x+1:]  
    platform[y] = platform[y][:x+1] + "O" + platform[y][x+2:]

def tilt(direction):
    previousPlatform = hash(tuple(platform))
    while True:
        for i in range(len(listO)):
            y = listO[i][0]
            x = listO[i][1]
            if direction == "up":
                moveUp(y,x,i)
            elif direction == "down":
                moveDown(y,x,i)
            elif direction == "left":
                moveLeft(y,x,i)
            elif direction == "right":  
                moveRight(y,x,i)
        if hash(tuple(platform)) == previousPlatform:
            break
        previousPlatform = hash(tuple(platform))

seen = []
test=True
ah = 0
firstFound = tuple()
for i in range(1000000000):
    tilt("up")
    tilt("left")
    tilt("down")
    tilt("right")
    
    if tuple(platform) in seen and test:
        ah=i
        firstFound = tuple(platform)
        test=False
        continue
    if tuple(platform) == firstFound:
        print("start",ah,"end",i)
        cycleLeft = (1000000000-ah-1)%(i-ah)
        for i in range(cycleLeft):
            tilt("up")
            tilt("left")
            tilt("down")
            tilt("right")
        break
    seen.append(tuple(platform))

sum=0
for O in listO:
    sum+=len(platform)-O[0]

print(sum)
