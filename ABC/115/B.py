# -*- coding: utf-8 -*-
p = []
for n in range(int(input())):
    p.append(int(input()))

max_value = max(p)
p.remove(max_value)
print(int(max_value / 2) + sum(p))
