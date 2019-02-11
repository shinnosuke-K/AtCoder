# -*- coding: utf-8 -*-
num_list = [0, 0, 0, 0]
for n in range(3):
    a, b = map(int, input().split())
    num_list[a - 1] += 1
    num_list[b - 1] += 1

if 3 in num_list:
    print('NO')
else:
    print('YES')