import math

file1 = open("./day4/input.txt", "r")

lines = file1.readlines()
file1.close()
res = 0

sum=0

for line in lines:
    line = line.split(":")[1]
    line = line.split("|")
    winning = line[0]
    numbers = line[1]
    winning = winning.split(" ")
    numbers = numbers.split(" ")
    #remove \n from last element
    numbers[-1] = numbers[-1].replace("\n", "")
    common = set(winning).intersection(numbers)
    common.discard('')
    if len(common)-1 >= 0:
        sum +=int( math.pow(2, len(common)-1))

print(sum)