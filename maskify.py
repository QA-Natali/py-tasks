# maskify - ky8 - kata
# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

def maskify(cc):
    if len(cc) <= 4:
        return cc
    else:
        a = len(cc) - 4
        b = ''
        for i in cc:
            if a > 0:
                b += '#'
                a -= 1
            else:
                b += i
        return b