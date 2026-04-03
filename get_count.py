# get_count.py - get_count - ky8 - kata
# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

def get_count(sentence):
    list = ['a', 'e', 'i', 'o', 'u']
    x = 0
    for i in sentence:
        if i in list:
            x += 1
    return x