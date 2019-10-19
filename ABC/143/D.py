#!/usr/bin/env python
N = int(input())
L = list(map(int, input().split()))
count = 0
L.sort()
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            if L[k] < L[i]+L[j]:
                count += 1
            else:
                break

print(count)
