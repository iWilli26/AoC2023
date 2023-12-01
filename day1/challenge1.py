import re

file1 = open("./input.txt", "r")

lines = file1.readlines()
res = 0
for line in lines:
    numbers = re.sub("[^0-9]", "", line)
    if len(numbers) == 1:
        res += int(numbers + numbers) 
    else:
        res += int(numbers[0] + numbers[-1])
print(res)
file1.close()


