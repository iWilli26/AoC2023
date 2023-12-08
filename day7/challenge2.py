file1 = open("./day7/input.txt", "r")
lines = file1.readlines()
file1.close()

def card_value(card):
    if card.isdigit():
        return int(card)
    elif card == 'T':
        return 10
    elif card == 'J':
        return 1
    elif card == 'Q':
        return 12
    elif card == 'K':
        return 13
    elif card == 'A':
        return 14
    else:
        raise ValueError(f"Invalid card: {card}")
    
levels = {
    "FiveOfAKind" : [],
    "FourOfAKind" : [],
    "FullHouse" : [],
    "ThreeOfAKind" : [],
    "TwoPairs" : [],
    "OnePair" : [],
    "HighCard" : [],
}

for line in lines:
    hand = line.split(" ")[0]    

    bid = line.split(" ")[1].replace("\n","")
    handDict = {
        "":0,
        "2":0,
        "3":0,
        "4":0,
        "5":0,
        "6":0,
        "7":0,
        "8":0,
        "9":0,
        "T":0,
        "J":0,
        "Q":0,
        "K":0,
        "A":0,
    }
    for card in hand:
        handDict[card] += 1
        
    handWithModifiedJ = hand
    if "J" in hand:
        mostPresent = ""
        mostPresentList = []
        for key in handDict:
            if handDict[key] > handDict[mostPresent] and key != "J":
                mostPresent = key
                mostPresentList = [key]
            elif handDict[key] == handDict[mostPresent] and key != "J":
                mostPresentList.append(key)
        if len(mostPresentList) == 13:
            mostPresentList = ["A"]

        highest = "0"
        for card in mostPresentList:
            if card_value(card) > card_value(highest):
                highest = card

        handWithModifiedJ = hand.replace("J", highest)

    handDict = {
        "":0,
        "2":0,
        "3":0,
        "4":0,
        "5":0,
        "6":0,
        "7":0,
        "8":0,
        "9":0,
        "T":0,
        "J":0,
        "Q":0,
        "K":0,
        "A":0,
    }

    for card in handWithModifiedJ:
        handDict[card] += 1

    if list(handDict.values()).count(5)>0:
        levels["FiveOfAKind"].append({"hand":hand, "handJ": handWithModifiedJ ,"bid":bid})
        continue
    if list(handDict.values()).count(4)>0:
        levels["FourOfAKind"].append({"hand":hand, "handJ": handWithModifiedJ, "bid":bid})
        continue
    if list(handDict.values()).count(3)==1:
        if list(handDict.values()).count(2)==1:
            levels["FullHouse"].append({"hand":hand,"handJ": handWithModifiedJ,  "bid":bid})
            continue
        else:
            levels["ThreeOfAKind"].append({"hand":hand, "handJ": handWithModifiedJ, "bid":bid})
            continue
    if list(handDict.values()).count(2)==2:
        levels["TwoPairs"].append({"hand":hand, "handJ": handWithModifiedJ, "bid":bid})
        continue
    if list(handDict.values()).count(2)==1:
        levels["OnePair"].append({"hand":hand, "handJ": handWithModifiedJ, "bid":bid})
        continue
    if list(handDict.values()).count(1)==5:
        levels["HighCard"].append({"hand":hand, "handJ": handWithModifiedJ, "bid":bid})
        continue
order = []



def sorting_key(item):
    return [card_value(card) for card in item['hand']]

for level in list(levels.keys()):

    sorted_data = sorted(levels[level], key=sorting_key, reverse=True)
    for item in sorted_data:
        order.append(item)

order.reverse()

sum = 0
for i in range(0, len(order)):
    sum += int(order[i]["bid"])*(i+1)
print(sum)