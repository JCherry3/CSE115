#Math Caluclator
#You should find all functions you need here for precalc

import math

def hypotenuse(a,b):
    return math.sqrt(a*a+b*b)

def cdist(x1,y1,x2,y2):
    #for points on the cartesian plane
    d1=abs(x2-x1)
    d2=abs(y2-y1)
    root = d1*d1+d2*d2
    distance = math.sqrt(root)
    return f"Root {root} or {distance}"

def slope(x1,y1,x2,y2):
    #for points on the cartesian plane
    x=abs(x2-x1)
    y=abs(y2-y1)
    return y/x

def genslope(x,y):
    return (-x)/y

def quadroot(a,b,c):
    #When ax^2+bx+c=0
    posb = (-b + math.sqrt((b*b)-4*a*c))/(2*a)
    negb = (-b - math.sqrt((b*b)-4*a*c))/(2*a)
    return f"{posb} and {negb}"

def perpendicular(x):
    return -1/x

def parabola(xv,yv,x1,y1):
    #to find a parabolas vertex form given a point and vertex
    a = (y1-yv)/((x1-xv)*(x1-xv))
    if a == 1:
        answer = f"(x-{xv})^2 + ({yv})"
    else:
        answer = f"{a}(x-{xv})^2 + ({yv})"
    return answer

def circle(xc,yc,x1,y1):
    radius = cdist(xc,yc,x1,y1)
    return f"(x-{xc})^2+(y-{yc})^2 = ({radius})^2"
