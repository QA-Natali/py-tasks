# small_enough - ky7 - kata
# https://www.codewars.com/kata/57cc981a58da9e302a000214/train/python

def small_enough(array, limit):
    array.sort()
    if array[-1] <= limit:
        return True
    else:
        return False