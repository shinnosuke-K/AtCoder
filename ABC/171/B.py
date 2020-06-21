n, k = map(int, input().split())
p = list(map(int, input().split()))

p.sort()
mon = 0
for i in range(k):
    mon += p[i]
print(mon)