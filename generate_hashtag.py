# generate_hashtag - ky5 - kata
# https://www.codewars.com/kata/52449b062fb80683ec000024/train/python

def generate_hashtag(s):
    answer = ''
    isSpaces = True 
    x = 0
    for i in s:
        if i == ' ':
            isSpaces = True
        else:
            x += 1
            if isSpaces == True:
                answer += i.upper()
                isSpaces = False
            else:
                answer += i.lower()
        if x > 139:
               break
    if x > 139 or x == 0:
        return False
    else:
        return '#' + answer