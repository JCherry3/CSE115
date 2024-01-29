import random

def secretSanta(famdict):
    ans = []
    count = 0
    stop = 0
    for key in famdict:
        l = famdict[key]
        random.shuffle(l)
        famdict[key] = l
        if(len(l) > stop):
            stop = len(l)
    while(count < stop):
        for key in famdict:
            plist = famdict[key]
            for val in plist:
                if(val not in ans):
                    ans.append(val)
                    break
        count = count + 1
    return ans
