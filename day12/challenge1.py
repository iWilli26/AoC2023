import math
from itertools import combinations
file1 = open("./day12/input.txt", "r")
lines = file1.readlines()
file1.close()

def generate_combinations(n, h):
    if h > n:
        return []
    indices_combinations = list(combinations(range(n), h))

    result = []

    for indices in indices_combinations:
        boolean_array = [False] * n
        for index in indices:
            boolean_array[index] = True
        result.append(boolean_array)

    return result

def test_line(line, combi, guide):
    sum = 0
    for combination in combi:
        modifiedLine = list(line)
        counter = 0
        for i in range(len(modifiedLine)):
            if modifiedLine[i] == "?" and combination[counter] == True:
                modifiedLine[i] = "#"
                counter += 1
            elif modifiedLine[i] == "?" and combination[counter] == False:
                modifiedLine[i] = "."
                counter += 1
            else:
                pass
        # print(modifiedLine)
        groupedHashtag = "".join(modifiedLine).split(".")
        result =[]
        for element in groupedHashtag:
            if element != "":
                result.append(len(element))
        if result == guide:
            sum += 1
    return sum

res = 0
for line in lines:
    line = line.strip()
    line = line.split(" ")
    map = line[0]
    guide = line[1].split(",")
    guide = [int(element) for element in guide]
    unknown = map.count("?")
    springs = map.count("#")
    combi = generate_combinations(unknown,sum(guide)- springs)
    res += test_line(map, combi, guide)
print(res)
