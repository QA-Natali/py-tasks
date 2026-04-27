# remove_url_anchor - ky7- kata
# https://www.codewars.com/kata/51f2b4448cadf20ed0000386/train/python

def remove_url_anchor(url):
    answer = ''
    for i in url:
        if i == '#':
            break
        answer += i 
    return answer