import math

def par(a, b, c, w):
    result = a * b * c
    return "{:.{}f}".format(result, w)

def pir(a, b, c, w):
    result = (a * b * c)/3
    return "{:.{}f}".format(result, w)

def cil(a, b, w):
    result = math.pi * a * b * 2
    return "{:.{}f}".format(result, w)