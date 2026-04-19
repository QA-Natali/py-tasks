# odd_or_even - ky7 - kata
# https://www.codewars.com/kata/5949481f86420f59480000e7/train/python

def odd_or_even(arr):
    sum = 0
    for i in arr:
        sum += i
    if sum % 2 == 0:
        return'even'
    else:
        return'odd'