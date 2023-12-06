import math
import re

file1 = open("./day6/input.txt", "r")
lines = file1.readlines()
file1.close()

time = re.findall(r'\b\d+\b', lines[0])
time= list(map(int, time))
print(time)

distance = re.findall(r'\b\d+\b', lines[1])
distance = list(map(int, distance))
print(distance)
res = 1
for i in range(len(distance)):
    sum = 0
    timeRace = int(time[i])
    distanceRace = int(distance[i])
    for second_held in range(timeRace):
        speed = second_held
        distance_traveled = (timeRace - second_held) * speed
        if distance_traveled >= distanceRace:
            sum += 1
    res*=sum
print(res)            