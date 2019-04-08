# -*- coding: utf-8 -*-

s = int(input())
n = 1
while s != 4:
    if s % 2 == 0:
        s = int(s / 2)
    else:
        s = 3 * s + 1
    n += 1

print(n + 3)