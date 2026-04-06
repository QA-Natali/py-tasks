# move_zeros - ky5 - kata
# https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python

def move_zeros(lst):
    new_list = []
    zero_list = []
    for i in lst:
        if i == 0:
            zero_list.append(i)
        else:
            new_list.append(i)
    return new_list + zero_list