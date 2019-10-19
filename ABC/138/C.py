# -*- coding: utf-8 -*-
n = int(input())
v = sorted(list(map(float, input().split())))

while len(v) > 1:
    v.insert(0, (v.pop(0) + v.pop(0)) / 2)

print(v[0])