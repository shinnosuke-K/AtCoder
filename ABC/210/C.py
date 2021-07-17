from collections import defaultdict
n, k = map(int, input().split())
c = list(map(int, input().split()))

ans = 0
dup = 0

for i in range(0, n - k+1):
    d = defaultdict(int)

    for j in range(k):
        d[c[i+j]] += 1
        if i != 0 and dup <= max(d.values()):
            break
    dup = max(d.values())
    if ans <= len(d):
        ans = len(d)
print(ans)