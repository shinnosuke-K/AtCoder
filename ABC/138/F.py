# -*- coding: utf-8 -*-
l, r = map(int, input().split())
count = 0

for x in range(l, r + 1):
    for y in range(l, r + 1):
        if (x % y) == (x ^ y):
            count += 1
            print(count)

print(count % (10**9 + 7))
