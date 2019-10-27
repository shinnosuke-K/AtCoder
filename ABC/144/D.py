import math

a, b, x = map(int, input().split())

if (a * a * b) / 2 >= x:
    tan = (a * b * b) / (2 * x)
    print(math.degrees(math.atan(tan)))
else:
    tan = 2 * ((a * a * b) - x) / (a * a * a)
    print(math.degrees(math.atan(tan)))
