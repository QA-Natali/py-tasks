# solution - ky6 -  kata
# https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

def solution(number):
    x = 0
    for i in range(number):
        if (i % 3 == 0) or (i % 5 == 0):
            x += i
    return x