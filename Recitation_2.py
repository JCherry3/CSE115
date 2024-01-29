#Recitation 2

import math

#Calculates time by dividing distance by rate
def timeNeeded(rate,distance):
    time = distance/rate
    return time

#Converts the length of something from inches to feet
def printLength(inches):
    feet = inches//12
    inches = inches-(feet*12)
    answer = "{} feet and {} inches".format(feet,inches)
    return answer

#Calculates the height of a tree by using the distance from the tree
def treeHeight(angle,dist):
    height = dist * (math.sin(angle))
    return height
