# filter_list - ky7 - kata
# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

def filter_list(l):
    n_l = []
    for i in l:
        if type(i) == int:
            n_l.append(i)
    return n_l