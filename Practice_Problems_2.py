#Module 2 Programming Problems

def postage(weight):
    if(weight <= 3.5):
        price = 1.38
    if(weight <= 3):
         price = 1.14
    if(weight <= 2):
        price = 0.90
    if(weight <= 1):
        price = 0.66
    if((weight < 0) or (weight > 3.5)):
        price = None
    return price

def bp_category(diastolic,systolic):
    reading = None
    if(diastolic < 80):
        if(systolic < 120):
            reading = "normal"
        if((systolic >= 120) and (systolic < 130)):
            reading = "elevated"
    if(((diastolic >= 80) and (diastolic < 90)) or ((systolic >= 130) and (systolic < 140))):
        reading = "hypertension stage 1"
    if((diastolic >= 90) or (systolic >= 140)):
        reading = "hypertension stage 2"
    return reading

def first_longest(slist):
    longest = ""
    for x in slist:
        if(len(x) > len(longest)):
            longest = x
    return longest

def last_longest(slist):
    longest = ""
    for x in slist:
        if(len(x) >= len(longest)):
            longest = x
    return longest

def total_length(slist):
    length = 0
    for x in slist:
        length = length + len(x)
    return length

def is_member(string,slist):
    for x in slist:
        if(x == string):
            return True
    return False

def zip(l1,l2):
    l3 = []
    y = 0
    for x in l1:
        l3.append(x)
        l3.append(l2[y])
        y = y+1
    return l3

def unzip(list1):
    list2 = []
    list3 = []
    index = 0
    for x in list1:
        if((index % 2) == 0):
            list2.append(x)
        else:
            list3.append(x)
        index = index + 1
    biglist = [list2, list3]
    return biglist

def oddValuesSum(numlist):
    total = 0
    for x in numlist:
        check = x % 2
        if(check == 1):
            total = total + x
    return total

def oddIndexSum(numlist):
    total = 0
    index = 0
    for x in numlist:
        if((index % 2) == 1):
            total = total + x
        index =  index + 1
    return total

def longStrings(slist):
    newlist = []
    for x in slist:
        if(len(x) > 4):
            newlist.append(x)
    return newlist

def long_N_Strings(slist,length):
    newlist = []
    for x in slist:
        if(len(x) > length):
            newlist.append(x)
    return newlist

def chooser(slist,blist):
    newlist = []
    index = 0
    for x in blist:
        if(x == True):
            newlist.append(slist[index])
        index = index + 1
    return newlist

def intersection(l1,l2):
    newlist = []
    for x in l1:
        if(is_member(x,l2) == True):
            if(is_member(x,newlist) == False):
                newlist.append(x)
    return newlist

def difference(l1,l2):
    newlist = []
    for x in l1:
        if(is_member(x,l2) == False):
            if(is_member(x,newlist) == False):
                newlist.append(x)
    return newlist

def plusOne(numlist):
    index = 0
    for x in numlist:
        numlist[index] = x+1
        index = index + 1
    return None
