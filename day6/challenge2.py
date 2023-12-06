import math
import re

file1 = open("./day6/input.txt", "r")
lines = file1.readlines()
file1.close()

time = re.findall(r'\b\d+\b', lines[0])

distance = re.findall(r'\b\d+\b', lines[1])

sum = 0
timeRace = int(time[0])
distanceRace = int(distance[0])
for second_held in range(timeRace):
    speed = second_held
    distance_traveled = (timeRace - second_held) * speed
    if distance_traveled >= distanceRace:
        sum += 1
print(sum)            