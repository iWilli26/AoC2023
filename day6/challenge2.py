import math
import re

file1 = open("./day6/input.txt", "r")
lines = file1.readlines()
file1.close()

time = re.findall(r'\b\d+\b', lines[0])
time= list(map(int, time))
newTime =""
for i in range(len(time)):
    newTime = newTime + str(time[i]) 

distance = re.findall(r'\b\d+\b', lines[1])
distance = list(map(int, distance))
newDistance =""
for i in range(len(distance)):
    newDistance = newDistance + str(distance[i]) 

sum = 0
timeRace = int(newTime)
distanceRace = int(newDistance)
for second_held in range(timeRace):
    speed = second_held
    distance_traveled = (timeRace - second_held) * speed
    if distance_traveled >= distanceRace:
        sum += 1
print(sum)            