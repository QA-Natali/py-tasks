# rgb - ky5 - kata
# https://www.codewars.com/kata/513e08acc600c94f01000001/train/python

def hexIt(number):
    if number < 0:
        number = 0
    if number > 255:
        number = 255
    number = hex(number)
    if len(number) == 3:
        return '0' + number[-1].upper()
    else:
        return number[-2:].upper()

def rgb(r, g, b):
    return hexIt(r) + hexIt(g) + hexIt(b)