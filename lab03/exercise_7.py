from math import sqrt

def point_distance(x0, y0, x1, y1):
    return sqrt((x1-x0)**2 + (y1-y0)**2)

print(point_distance(-2, 1, 1, 5))
