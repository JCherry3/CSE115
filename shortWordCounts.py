#Short Word Counter

#Counts words of a certain length or less in a file
def shortWordCounts(filename, length):
    newdict = {}
    with open(filename, 'r') as file:
        for line in file:
            line1 = line.rstrip('\r\n')
            linelist = line1.split(' ')
            for x in linelist:
                if(len(x) <= length):
                    if((x in newdict) == False):
                        newdict[x] = 1
                    elif(x in newdict):
                        newdict[x] = newdict[x] + 1
    return newdict
