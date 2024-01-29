#Week 6

def distanceFrom(numlist,n):
    index = 0
    for x in numlist:
        numlist[index] = x-n
        index = index + 1
    return None

def strLength(slist):
    lenlist = []
    for x in slist:
        lenlist.append(len(x))
    return lenlist

def gradeCount(gradeInfo,letter):
    count = 0
    for x in gradeInfo:
        if(x == letter):
            count = count + 1
    return count

def courseGrades(gradeInfo):
    glist = ["A","B","C","D","F"]
    final = []
    for x in glist:
        final.append(x)
        count = gradeCount(gradeInfo,x)
        final.append(count)
    return final

def reverseStrLength(slist):
    lenlist = []
    for x in slist:
        lenlist = [len(x)] + lenlist
    return lenlist

def extractUBIT(slist):
    newlist = []
    for x in slist:
        ubit = ""
        for i in x:
            if(i != "@"):
                ubit = ubit + i
            if(i == "@"):
                newlist.append(ubit)
                break;
    return newlist
