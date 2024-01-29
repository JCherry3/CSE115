#Practice Programming Questions 1

import math

def r_perimeter(l,w):
    return l+l+w+w

def r_area(l,w):
    return l*w

def c_perimeter_radius(r):
    return 2*math.pi*r

def c_perimeter_diameter(d):
    circumference = d*math.pi
    return circumference

def c_area_radius(r):
    area = math.pi*r*r
    return area

def c_area_diameter(d):
    r = d/2
    area = math.pi*r*r
    return area

def how_much_paint(w,h,g):
    gallons = (w*h)/g
    return gallons

def how_many_paint_cans(w,h,g):
    gallons = (w*h)/g
    cans = math.ceil(gallons)
    return cans
