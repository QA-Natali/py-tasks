# descending_order - ky8 - kata
# https://www.codewars.com/kata/5467e4d82edf8bbf40000155/train/python

def descending_order(num):
    num = list(str(num))
    num.sort(reverse=True)
    return  int("".join(num))