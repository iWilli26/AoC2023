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

def transform(seeds, source, destination, incr, changed):
    result = []
    for i in range(len(seeds)):
        if int(seeds[i]) == changed[i]:
            result.append(int(seeds[i]))
            continue
        if source<=int(seeds[i]) and int(seeds[i])<=source+incr-1:
            result.append(destination + int(seeds[i]) - source)
            changed[i]=destination + int(seeds[i]) - source
        else:
            result.append(int(seeds[i]))
    print("changed", changed)
    return result, changed

temp = []
for s in seeds:
    temp.append(int(s))
seeds = temp

print("seeds", seeds)

for map in maps:
    result = []
    changed = [""]*len(seeds)
    for line in map:
        source = int(line[1])
        destination = int(line[0])
        incr = int(line[2])
        seeds, changed = transform(seeds, source, destination, incr, changed)
        result.append(seeds)
    
    print(seeds)

lowest = math.inf
for seed in seeds:
    if int(seed)<lowest:
        lowest = int(seed)
print(lowest)