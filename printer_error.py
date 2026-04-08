# printer_error - ky7 - kata
# https://www.codewars.com/kata/56541980fa08ab47a0000040/train/python

def printer_error(s):
    letters = ["n","o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    error = 0
    for i in s:
        if i in letters:
            error += 1
    return str(error) + '/' + str(len(s))