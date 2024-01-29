#Week 5

import math

def timesThree(a,b):
    return (a == (b*3))

numlist = [30,4,17,1,23,9,-4,3,15]

def sumList(List):
    total = 0
    for x in List:
        total = total + x
        print(f"running total is {total}")

def productList(List):
    total = 0
    for x in List:
        if(total == 0):
            total = x
        else:
            total = total * x
        print(f"running total is {total}")

def count_Matching(numlist,num):
    matches = 0
    for x in numlist:
        if(x == num):
            matches = matches + 1
    return matches

def filter_by_length(slist,length):
    newlist = []
    for x in slist:
        if(len(x) = length):
            newlist.append(x)
    return newlist
