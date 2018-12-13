# -*- coding: utf-8 -*-
x = int(input())
sum_x = 0
for n in range(1, 10 ** 9 + 1):
    sum_x += n
    if sum_x >= x:
        print(n)
        break