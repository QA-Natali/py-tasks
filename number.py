# number - ky7 - kata
# https://www.codewars.com/kata/54bf85e3d5b56c7a05000cf9/train/python

def number(lines):
    n = 1
    r = []
    for i in lines:
        r.append(str(n) + ': ' + i)
        n += 1
    return r 