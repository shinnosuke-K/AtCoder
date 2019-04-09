# -*- coding: utf-8

input()
x=s=0
for n in list(map(int, input().split())):
    s += max(n-x, 0)
    x = n
print(s)