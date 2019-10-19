#!/usr/bin/env python
N = int(input())
S = list(input())
count = 1
word = S[0]
for i in range(1, N):
    if word != S[i]:
        count += 1
        word = S[i]

print(count)