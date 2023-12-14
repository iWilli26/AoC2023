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

def count_differences(string1, string2):
    # Ensure the strings have the same length
    if len(string1) != len(string2):
        raise ValueError("Input strings must have the same length")

    differences = 0
    for ch1, ch2 in zip(string1, string2):
        if ch1 != ch2:
            differences += 1
    return differences

characterReflection = 0
sum = 0
for pattern in patterns:
    for whereColumn in range(1,len(pattern)):
        test = min(len(pattern[:whereColumn]), len(pattern[whereColumn:]))
        top = pattern[(whereColumn-test):whereColumn][:test]
        bottom = pattern[whereColumn:][:test]

        sumDiff=0
        for i in range(len(top)):
            sumDiff += count_differences(list(top[i]), list(bottom[::-1][i]))
        
        # sumDiff += count_differences(list(top), list(bottom))
        
        if sumDiff == 1:
            sum+=whereColumn*100
            for j in range(len(pattern[(whereColumn-test):whereColumn][:test])):    
                print(pattern[(whereColumn-test):whereColumn][:test][j])
            print("----------------")
            for j in range(len(pattern[whereColumn:][:test])):
                print(pattern[whereColumn:][:test][j])
            print("\n")
    
    for whereLine in range(1, len(pattern[0])):#for every vertical mirrors
        lineReflection = 0
        sumDiff=0

        for i in range(len(pattern)):#for each line
            characterReflection = 0
            test = min(whereLine, len(pattern[i])-whereLine)
            
            # print(pattern[i][:whereLine] + "|" + pattern[i][whereLine:],test)
            left = pattern[i][whereLine-test:whereLine]
            right = pattern[i][whereLine:whereLine+test]
            # print(left)
            # print(right)

            sumDiff += count_differences(list(left), list(right[::-1]))

            if left == right[::-1]:
                lineReflection += 1

        if sumDiff == 1:
            for j in range(len(pattern)):    
                print(pattern[j][:whereLine] + "|" + pattern[j][whereLine:])
            print("\n")
            sum+=whereLine
            break

    
        

print(sum)
            
# print(count_differences("abaa", "bbbb"))