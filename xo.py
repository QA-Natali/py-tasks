# xo - ky8 - kata
# https://www.codewars.com/kata/55908aad6620c066bc00002a/train/python

def xo(s):
    s  = s.lower()
    a = 0
    b = 0
    for i in s:
        if i == 'x':
            a += 1
        if i == 'o':
            b += 1
    if a == b:
        return True
    else:
        return False