file1 = open("./day9/input.txt", "r")
lines = file1.readlines()
file1.close()
    
def notSoRecursiveShit(values):
    newValues = []
    for i in range(len(values)-1):
        newValues.append(int(values[i+1]) - int(values[i]))
    return newValues

sum=0

for line in lines:
    visual = {}
    values = line.split(" ")
    values[-1] = values[-1].replace("\n","")
    newValues = [1]
    visual["0"] = values
    i=1
    while newValues.count(0) != len(newValues):    
        newValues = notSoRecursiveShit(values)
        values = newValues
        visual[str(i)] = values
        i+=1
    for i in range(len(visual.keys())-1,-1,-1):
        if i== len(visual.keys())-1:
            continue
        visual[str(i)].insert(0,int(visual[str(i)][0]) - int(visual[str(i+1)][0]))
    sum += visual["0"][0]
print(sum)
