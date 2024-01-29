#This brings in the python math module
import math
#This function will produce a number one greater than the input
def add_one(x):
    return x+1
#This function will return the average of three numbers
#Due to division, we expect floating point results
def average_three(a1,a2,a3):
    average=(a1+a2+a3)/3
    return average
#This function computes the pythagorean theorem and finds the hypotenuse
def hypotenuse(a,b):
    hyp= math.sqrt(a*a+b*b)
    return hyp
