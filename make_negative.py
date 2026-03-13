# make_negative - ky8 kata
# https://www.codewars.com/kata/55685cd7ad70877c23000102

def make_negative( number ):
    if number < 0:            # если меньше 0 
        return (number)       # возвращаем number
    else:                     # в любом другом случае
        return (number * -1)  # умножаем на -1 и получаем отрицательное число