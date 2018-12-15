# -*- coding: utf-8 -*-
s = list(input())
i = 0
count = 0
for n in range(len(s) - 1, -1, -1):
    if s[n] == 'B':
        count += (len(s) - i) - (n + 1)
        i += 1

print(count)