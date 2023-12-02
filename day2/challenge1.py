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
    encule = line.split(":")
    id= int(encule[0].split(" ")[1])
    fuck = encule[1].split(";")
    for i in range(len(fuck)):
        cubes = lineToCubes(fuck[i])
        dict = cubesToDict(cubes)
        if("red" in dict):
            if(dict["red"]>12):
                break
        if("blue" in dict):
            if(dict["blue"]>14):
                break
        if("green" in dict):
            if(dict["green"]>13):
                break
        if(i==len(fuck)-1):
            sum+=id
        
print(sum)


