import math
import sys

n = int(input())
ans = sys.maxsize
for i in reversed(range(1, math.sqrt(n).__int__() + 1)):
    if n % i == 0:
        cur = max(len(str(i)), len((str(n // i))))
        if ans > cur:
            ans = cur

if n == 1:
    print(1)
else:
    print(ans)
