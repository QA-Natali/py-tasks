# alphabet_war - ky7 - kata
# https://www.codewars.com/kata/59377c53e66267c8f6000027/train/python

def alphabet_war(fight):
    left = 0
    right = 0
    for letter in fight:
        if letter == 'w':
            left += 4
        elif letter == 'p':
            left += 3
        elif letter == 'b':
            left += 2
        elif letter == 's':
            left += 1
        elif letter == 'm':
            right += 4
        elif letter == 'q':
            right += 3
        elif letter == 'd':
            right += 2
        elif letter == 'z':
            right += 1
        else:
            pass
    if left > right:
        return 'Left side wins!'
    elif left < right:
        return 'Right side wins!'
    else: 
        return 'Let\'s fight again!'