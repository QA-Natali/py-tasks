# smash - ky8 - kata
# https://www.codewars.com/kata/53dc23c68a0c93699800041d/train/python

def smash(words):
    x = ' '
    for word in words:
         x+= word + ' '

    return x.strip()