import csv

def q1(filename):
    endlist = []
    with open(filename) as file:
        lines = list(csv.reader(file))
    header = lines[0]
    count = 0
    for line in lines:
        if(count > 0):
            newdict = {}
            for x in range(len(line)):
                newdict[header[x]] = line[x]
            endlist.append(newdict)
        count = count + 1
    return endlist

def q2(filename,records):
    header = list(records[0].keys())
    with open(filename,'w') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        for d in records:
            dlist = list(d.values())
            writer.writerow(dlist)
    return None

def q3(infile,outfile,titles):
    with open(infile) as file1:
        records = list(csv.reader(file1))
    headers = records[0]
    ilist = []
    for title in titles:
        for x in range(len(headers)):
            if(title == headers[x]):
                ilist.append(x)
    with open(outfile,'w') as file2:
        writer = csv.writer(file2)
        for record in records:
            newlist = []
            for i in ilist:
                newlist.append(record[i])
            writer.writerow(newlist)
    return None

def q4(infile,outfile,name,value):
    with open(infile) as file1:
        records = list(csv.reader(file1))
    headers = records[0]
    index = 0
    for x in range(len(headers)):
        if(headers[x] == name):
            index = x
    plist = []
    for record in records:
        if(record[index] == value):
            plist.append(record)
    with open(outfile,'w') as file2:
        writer = csv.writer(file2)
        writer.writerow(headers)
        for line in plist:
            writer.writerow(line)
    return None
