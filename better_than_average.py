# better_than_average - ky8 - kata
# https://www.codewars.com/kata/5601409514fc93442500010b/train/python

def better_than_average(class_points, your_points):
    x = 1
    y = your_points 
    for sum_points in class_points:
        x += 1
        y += sum_points
    return (y / x < your_points)