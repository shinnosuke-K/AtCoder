import math

a,b,c = map(int, input().split(" "))

if (a > 0 and b < 0) or (a < 0 and b > 0):
    if c % 2 == 0:
        ab = abs(a/b)
        if ab == 1:
            print("=")
        elif ab > 1:
            print(">")
        else:
            print("<")
    else:
        if a < 0:
            print("<")
        elif b < 0:
            print(">")
else:
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")