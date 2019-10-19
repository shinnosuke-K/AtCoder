# -*- coding: utf-8 -*-

s = list(map(str, input()))
for w in range(1, len(s), 2):
    if 'R' in s[w]:
        print("No")
        exit()

for w in range(0, len(s), 2):
    if 'L' in s[w]:
        print('No')
        exit()

print('Yes')