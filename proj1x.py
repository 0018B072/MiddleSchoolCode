import math
import numpy as np
print("WELCOME TO PROJ PHYS: 1")

def physics():
    list = [ ]
    maxLength = (15*10^23)
    while len(list) <= maxLength:
        i = int(input("Enter constant speed (mph): \n "))
        r = float(input("Enter distance wanted: \n "))
        n = input("Enter direction: \n")
        result = r/i
        print("It is going: ",result,"mph | ", n)
        if r == r:
            break
physics()