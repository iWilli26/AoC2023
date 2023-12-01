import time
import re
start_time = time.time()

file1 = open("./input.txt", "r")
lines = file1.readlines()
res = 0

for line in lines:
    line = line.replace("one", "one1one")
    line = line.replace("two", "two2two")
    line = line.replace("three", "three3three")
    line = line.replace("four", "four4four")
    line = line.replace("five", "five5five")
    line = line.replace("six", "six6six")
    line = line.replace("seven", "seven7seven")
    line = line.replace("eight", "eight8eight")
    line = line.replace("nine", "nine9nine")
    numbers = re.sub("[^0-9]", "", line)
    if len(numbers) == 1:
        res += int(numbers + numbers) 
    else:
        res += int(numbers[0] + numbers[-1])
print(res)
file1.close()

print("--- %s seconds ---" % (time.time() - start_time))
