#Weeks 7 and 8

def isvowel(letter):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    if(letter in vowels):
        return True
    else:
        return False

def piglatin(string):
    wordlist = string.split(' ')
    latinstring = ''
    for x in wordlist:
        word = ''
        v = False
        for y in x:
            if(isvowel(y) == True):
                v = True
        if(isvowel(x[0]) == True):
            if(x[len(x)-1] == "w"):
                word = word + x + "hay"
            else:
                word = word + x + "way"
        else:
            if(isvowel(x[1]) == True or x[1] == "y"):
               split = slice(1,len(x))
               word = word + x[split] + x[0] + "ay"
            else:
                if(isvowel(x[2]) == True or x[2] == "y"):
                    split = slice(2,len(x))
                    word = word + x[split] + x[0] + x[1] + "ay"
                else:
                    split = slice(3,len(x))
                    word = word + x[split] + x[0] + x[1] + x[2] + "ay"
        if(v == False):
            word = x
        latinstring = latinstring + ' ' + word
    latinstring = latinstring[slice(1,len(latinstring))]
    return latinstring

#Creates a List of bases in a DNA string
def identifyBases(seq):
    baseList = []
    for x in seq:
        if(x not in baseList):
            baseList.append(x)
    return baseList

