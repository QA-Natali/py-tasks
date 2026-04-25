# to_jaden_case - ky7 - kata
# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python

def to_jaden_case(string):
    x = True
    a = ''
    for i in string:
        if x == True:
            a += i.upper()
            x = False
        else:
            if i == ' ':
                a += i
                x = True
            else:
                a += i.lower()
    return a