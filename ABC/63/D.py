# 回数を二分探索で調べる
import math
N, A, B = map(int, input().split())
h = [int(input()) for _ in range(N)]
AB = A - B
T = 1
high = 10 ** 14
low = 0
while high - low > 1:
    mid = (high+low)//2
    if sum([math.ceil((h[n] - mid*B)/AB) if (h[n] - mid*B) > 0 else 0 for n in range(N)]) <= mid:
        high = mid
    else:
        low = mid
print(high)
