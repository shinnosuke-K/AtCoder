# -*- coding: utf-8 -*-
k, a, b = map(int, input().split())
biscuits = 1
money = 0
for n in range(k):
    if biscuits == a:
        biscuits -= a
        biscuits += b
        n += 1
    else:
        biscuits += 1
print(biscuits)