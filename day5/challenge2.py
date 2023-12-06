import math
import numpy as np

file1 = open("./day4/input.txt", "r")

lines = file1.readlines()
file1.close()
res = 0

sum=0
actualCard=0
cards = [1]*len(lines)
for line in lines:
    line = line.split(":")[1]
    line = line.split("|")
    winning = line[0]
    numbers = line[1]
    winning = winning.split(" ")
    numbers = numbers.split(" ")
    numbers[-1] = numbers[-1].replace("\n", "")
    common = set(winning).intersection(numbers)
    common.discard('')
    for j in range(actualCard+1, actualCard+len(common)+1):
        cards[j] += cards[actualCard]
    actualCard+=1

print(cards)
sum = np.sum(cards)
print(sum)