# string_to_array - ky8 - kata
# https://www.codewars.com/kata/57e76bc428d6fbc2d500036d/train/python

def string_to_array(s):
    answer = []
    x = ''
    for i in s:
        if i !=' ':
            x +=i
        else:
            answer.append(x)
            x=''
    answer.append(x)
    return answer