# Even or Odd - 8ky kata 
# https://www.codewars.com/kata/53da3dbb4a5168369a0000fe/train/python

def even_or_odd(number):
    if number % 2 == 0:                     # остаток равен 0
        return('Even')                      # верни Even
    else:                                   # если ничто не подошло выше
        return('Odd')                       # верни Odd
