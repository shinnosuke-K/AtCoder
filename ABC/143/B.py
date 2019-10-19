#!/usr/bin/env python
N = int(input())
d = list(map(int, input().split()))
n_sum = 0
for n in range(N):
    for i in range(n+1, len(d)):
        n_sum += d[i] * d[n]

print(n_sum)