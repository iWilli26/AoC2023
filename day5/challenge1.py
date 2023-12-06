import math

file1 = open("./day5/input.txt", "r")
lines = file1.readlines()
file1.close()

seeds = lines[0].split(":")[1].split(" ")
seeds = seeds[1:]
seeds[-1]=seeds[-1].replace("\n","")

temp = []
maps = []
for line in lines[2:]:
    if line == "\n" :
        maps.append(temp)
        temp = []
        continue
    elif line[0].isnumeric():
        temp.append(line.replace("\n","").split(" "))

def transform(seeds, source, destination, incr):
    result = []
    for seed in seeds:
        if source<=int(seed) and int(seed)<source+incr:
            result.append(destination + int(seed) - source)
        else:
            result.append(int(seed))
    return result

for map in maps:
    result = []
    for line in map:
        source = int(line[1])
        destination = int(line[0])
        incr = int(line[2])
        seeds = transform(seeds, source, destination, incr)
        result.append(seeds)
    
    #fuck it
    #faut pas faire ligne par ligne ??? sfqgze,smlfkazo
    print(seeds, map)

lowest = math.inf
for seed in seeds:
    if int(seed)<lowest:
        lowest = int(seed)
print(lowest)