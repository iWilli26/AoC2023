import math

file1 = open("./day13/input.txt", "r")
lines = file1.readlines()
file1.close()

patterns = []
pattern = []
for i in range(len(lines)):    
    if lines[i]=="\n":
        patterns.append(pattern)
        pattern = []
    elif i==len(lines)-1:
        lines[i] = lines[i].strip()
        pattern.append(lines[i])
        patterns.append(pattern)
    else:
        lines[i] = lines[i].strip()
        pattern.append(lines[i])

characterReflection = 0
sum = 0
for pattern in patterns:
    for whereLine in range(1, len(pattern[0])):#for every vertical mirrors
        lineReflection = 0
        for i in range(len(pattern)):#for each line
            characterReflection = 0
            for j in range(min(whereLine, len(pattern[i])-whereLine) ): 
                if pattern[i][whereLine-1-j] == pattern[i][whereLine+j]:
                    characterReflection += 1
            if characterReflection == min(len(pattern[i][:whereLine]), len(pattern[i][whereLine:])):
                    lineReflection += 1
        if lineReflection == len(pattern):
            for j in range(len(pattern)):    
                print(pattern[j][:whereLine] + "|" + pattern[j][whereLine:])
            print("\n")
            sum+=whereLine

    for whereColumn in range(1,len(pattern)):
        test = min(len(pattern[:whereColumn]), len(pattern[whereColumn:]))
        if(pattern[(whereColumn-test):whereColumn][:test] == pattern[whereColumn:][:test][::-1]):
            sum+=whereColumn*100
            for j in range(len(pattern[(whereColumn-test):whereColumn][:test])):    
                print(pattern[(whereColumn-test):whereColumn][:test][j])
            print("----------------")
            for j in range(len(pattern[whereColumn:][:test])):
                print(pattern[whereColumn:][:test][::-1][j])
            print("\n")
        

print(sum)