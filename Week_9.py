#Week 9

def print_file(filename):
    with open(filename) as file:
        for line in file:
            line = line.rstrip("\r\n")
            print(line)

def count_words(string,d):
    words = string.split(" ")
    

def count_file(filename):
    with open(filename) as file:
        dictionary = {}
        for line in file:
            line = line.rstrip("\r\n")

def median(a,b,c):
    if((a <= b <= c) or (a >= b >= c)):
        median = b
    elif((b <= a <= c) or (c >= a >= b)):
        median = a
    else:
        median = c
    return median
