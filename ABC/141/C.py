# -*- coding: utf-8 -*-
n, k, q = map(int, input().split())
c = [k - q for i in range(n)]
a = [int(input()) for i in range(q)]
for i in range(q):
    c[a[i] - 1] += 1

for i in range(n):
    if c[i] >= 1:
        print("Yes")
    else:
        print("No")

