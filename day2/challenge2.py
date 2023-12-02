import re

file1 = open("./input.txt", "r")

lines = file1.readlines()
file1.close()
res = 0

def cubesToDict(cubes):
    dict = {}
    for i in range(len(cubes)):
        if i%2==0:
            number = int(cubes[i])
        else:
            dict[cubes[i]]=number
    return dict

def lineToCubes(line):
    line =line.replace(",", "")
    line =line.replace(":", "")
    line = line.replace("\n", "")
    words = line.split(" ")
    return words[1:]

sum=0
for line in lines:
    UwU = line.split(":")
    id= int(UwU[0].split(" ")[1])
    bruh = UwU[1].split(";")
    max = {
        "red":0,
        "green":0,
        "blue":0
    }
    for i in range(len(bruh)):
        cubes = lineToCubes(bruh[i])
        dict = cubesToDict(cubes)
        for key in dict.keys():
            if(dict[key]>max[key]):
                max[key]=dict[key]
    times = 1
    for key in max.keys():
        times*=max[key]

    sum+=times
print(sum)

