#!/usr/bin/env python3
from decimal import *
#----------------------------------------------------------------------
def add(nbrs):
    result = 0
    for nb in nbrs:
        if "." in nb:
            result += Decimal(nb)
        else:
            result += int(nb) 
    return result

#----------------------------------------------------------------------
def division(nbrs):
    if 0 in nbrs:
        return("ERROR")
    else:
        first = 0
        result = 0
        for nb in nbrs:
            if first == 0:
                if "." in nb:
                    result += Decimal(nb)
                else :
                    result += int(nb)
                first = 1
            else:
                if "." in nb:
                    result /= Decimal(nb)
                else:
                    result /= int(nb)
    return result

        

#----------------------------------------------------------------------
def multiply(nbrs):
    result = 1
    for nb in nbrs:
        if "." in nb:
            result *= Decimal(nb)
        else:
            result *= int(nb)
    return result

#----------------------------------------------------------------------
def subtract(nbrs):
    result = 0
    first = 0
    for nb in nbrs:
        if first == 0:
            if "." in nb:
                result += Decimal(nb)
            else:
                result += int(nb)
            first = 1
        else:
            if "." in nb:
                result -= Decimal(nb)
            else:
                result -= int(nb)
    return result