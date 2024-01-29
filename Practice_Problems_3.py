#Module 3 Practice Problems

def q1(d):
    return d[max(d)]

def q2(d,num):
    newlist = []
    for k in d:
        if(d[k] == num):
            newlist.append(k)
    return newlist

def q3(dlist,string):
    newlist = []
    for d in dlist:
        if(string in d):
            newlist.append(d)
    return newlist

def q4(dlist,num):
    newlist = []
    for d in dlist:
        for k in d:
            if(d[k] == num):
                newlisty.append(d)
    return newlist

def q5(d1,d2):
    ndict = {}
    for k in d1:
        if(k in d2):
            ndict[k] = d1[k] + d2[k]
    return ndict

def q6(d1,d2):
    ndict = {}
    for k in d1:
        if(k in d2):
            l = [d1[k],d2[k]]
            ndict[k] = l
    return ndict

def q7(file):
    wordlist = []
    with open(file,'r') as file:
        for line in file:
            line = line.rstrip('\n')
            linelist = line.split(' ')
            for word in lineslist:
                if(word not in wordlist):
                    wordlist.append(word)
    return wordlist

def q8(f1,f2):
    with open(f2,'w') as f2:
        f2.truncate(0)
        with open(f1,'r') as f1:
            for line in f1:
                f2.write(line)
    return None

def q9(f1,f2):
    newdict = {}
    with open(f1,'r') as f1:
        for line in f1:
            line = line.rstrip('\n')
            linelist = line.split(' ')
            for x in linelist:
                if((x in newdict) == False):
                    newdict[x] = 1
                elif(x in newdict):
                    newdict[x] = newdict[x] + 1
        wdict = sorted(newdict.items(),key = lambda x: x[1],reverse = True)
        wdict = dict(wdict)
        wordlist = []
        count = 0
        for key in wdict:
            if(count < 10):
                wordlist.append(key)
            count = count + 1
        with open(f2,'w') as f2:
            f2.truncate(0)
            for w in wordlist:
                ans = w + ' '
                f2.write(ans)
    return None

def q10(f1,f2):
    newname = f'{f1}{f2}'
    with open(f1,'r') as f1:
        f1lines = f1.readlines()
        with open(f2,'r') as f2:
            f2lines = f2.readlines()
            with open(newname,'w') as file:
                file.truncate(0)
                if(len(f1lines) > len(f2lines)):
                    for x in range(len(f1lines)):
                        line1 = f1lines[x]
                        file.write(line1)
                        if(x in range(len(f2lines))):
                            line2 = f2lines[x]
                            file.write(line2)
                        else:
                            file.write('\n')
                else:
                    for x in range(len(f2lines)):
                        if(x in range(len(f1lines))):
                            line2 = f1lines[x]
                            file.write(line2)
                        else:
                            file.write('\n')
                        line1 = f2lines[x]
                        file.write(line1)
    return None

def q11(filename,n):
    with open(filename,'r') as file:
        lines = file.readlines()
    for x in range(1,n+1):
        filesplit = filename.split('.')
        newfile = f'{filesplit[0]}{x}.{filesplit[1]}'
        with open(newfile,'w') as nfile:
            for i in range(0,len(lines),x):
                nfile.write(lines[i])
    return None

def q12(filename):
    filesplit = filename.split('.')
    vowels = f'{filesplit[0]}.vowels.{filesplit[1]}'
    consonants = f'{filesplit[0]}.consonants.{filesplit[1]}'
    others = f'{filesplit[0]}.others.{filesplit[1]}'
    def isvowel(letter):
        v = ['a','e','i','o','u','y','A','E','I','O','U','Y']
        if(letter in v):
            return True
        else:
            return False
    def isconsonant(letter):
        c = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z', 'B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Z']
        if(letter in c):
            return True
        else:
            return False
    def isother(letter):
        if((isconsonant(letter) == False) and (isvowel(letter) == False)):
            return True
        else:
            return False
    with open(filename,'r') as file:
        lines = file.readlines()
        
    with open(vowels,'w') as vowels:
        for line in lines:
            for char in line:
                if(isvowel(char) == True):
                    vowels.write(char)
    with open(consonants,'w') as consonants:
        for line in lines:
            for char in line:
                if(isconsonant(char) == True):
                    consonants.write(char)
    with open(others,'w') as others:
        for line in lines:
            for char in line:
                if(isother(char) == True):
                    others.write(char)
    return None
