import re

file1 = open("./input.txt", "r")
digits = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
]
lines = file1.readlines()
res = 0
for line in lines:
    line = line.replace("one", "1")
    line = line.replace("two", "2")
    line = line.replace("three", "3")
    line = line.replace("four", "4")
    line = line.replace("five", "5")
    line = line.replace("six", "6")
    line = line.replace("seven", "7")
    line = line.replace("eight", "8")
    line = line.replace("nine", "9")
    numbers = re.sub("[^0-9]", "", line)
    if len(numbers) == 1:
        res += int(numbers + numbers) 
    else:
        res += int(numbers[0] + numbers[-1])
print(res)
file1.close()


