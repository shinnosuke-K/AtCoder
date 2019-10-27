n, k = map(int, input().split())
a = list(map(int, input().split()))
f = list(map(int, input().split()))
a.sort()
f.sort(reverse=True)
time = [a[i] * f[i] for i in range(n)]

for i in range(k):
    index_time = time.index(max(time))
    time[index_time] -= f[index_time]
print(max(time))
