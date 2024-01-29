#CS115 Final Project

#Part 1

#It should return a list of all values stored in records associated with the key key.
def getValuesForKey(key,records):
    vlist = []
    for d in records:
        if(key in d):
            if((d[key] in vlist) == False):
                vlist.append(d[key])
    return vlist

#It should return the number of records whose value associated with the passed in key matches the passed in value.
def countMatchesByKey(key,value,records):
    count = 0
    for d in records:
        if(key in d):
            if(d[key] == value):
                count = count + 1
    return count

#It should return the number of records whose value associated with the key1 matches value1 AND whose value associated with key2 matches the value2 .
def countMatchesByKeys(key1,value1,key2,value2,records):
    count = 0
    for d in records:
        if((key1 in d) and (key2 in d)):
           if((d[key1] == value1) and (d[key2] == value2)):
                count = count + 1
    return count

#It should return a new list of dictionaries corresponding to the records whose value associated with the passed in key matches the passed in value.
def filterByKey(key,value,records):
    vlist = []
    for d in records:
        if(key in d):
            if(d[key] == value):
                vlist.append(d)
    return vlist

#It should return a dictionary where the keys are all of the values in records associated with key, and the values are the number of times that value appears in records.
def computeFrequency(key,records):
    ndict = {}
    for d in records:
        if(key in d):
            if(d[key] not in ndict):
                 ndict[d[key]] = 0
            if(d[key] in ndict):
                ndict[d[key]] = ndict[d[key]] + 1
    return ndict

#Part 2

#Imports the csv library
import csv

#It should return the list of dictionaries whose keys are the list of keys passed in as the first parameter, and whose values come from the corresponding list in values.
def convertToDictionaries(keys,vals):
    dlist = []
    for v in vals:
        ndict = {}
        for x in range(len(v)):
            ndict[keys[x]] = v[x]
        dlist.append(ndict)
    return dlist

#It should return a list, which contains one list for each non-header row in the CSV file.
def loadRecords(file):
    with open(file) as file:
        readfile = csv.reader(file)
        rows = []
        count = 0
        for row in readfile:
            if(count > 0):
                rows.append(row)
            count = count + 1
    return rows

#It should return a list of lists. Each list corresponds to one of the dictionaries in the 2nd parameter, and the values in the list correspond to the values in the dictionary
def convertToLists(keys,dlist):
    blist = []
    for d in dlist:
        slist = []
        for k in keys:
            if(k in d):
                slist.append(d[k])
            else:
                slist.append('')
        blist.append(slist)
    return blist

#It should return None, and append the records in the second parameter to the end of the csv file represented by the first parameter.
def writeRecords(file,records):
    with open(file,'a+') as file:
        count = 1
        for l in records:
            length = len(l)
            for x in range(length):
                file.write(l[x])
                if(x < (length - 1)):
                    file.write(',')
            if(count < len(records)):
                file.write('\n')
            count = count + 1
    return None
