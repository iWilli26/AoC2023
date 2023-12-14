import math

file1 = open("./day14/input.txt", "r")
lines = file1.readlines()
file1.close()

platform = []
for i in range(len(lines)):    
    platform.append(lines[i].strip())

def moveUp(y,x):
    if y==0 or platform[y-1][x] == "O" or platform[y-1][x] == "#":
        return
    platform[y] = platform[y][:x] + "." + platform[y][x+1:]  
    platform[y-1] = platform[y-1][:x] + "O" + platform[y-1][x+1:]
for plat in platform:
    print(plat)
print("\n")

previousPlatform = platform.copy()
sum=0
while True:
    for y in range(len(platform)):
        for x in range(len(platform[y])):
            if platform[y][x] == "O":
                moveUp(y,x)
    if platform == previousPlatform:
        for y in range(len(platform)):
            for x in range(len(platform[y])):
                if platform[y][x] == "O":
                    sum+=len(platform)-y
        break
    previousPlatform = platform.copy()

print(sum)