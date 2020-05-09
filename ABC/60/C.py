N, T = map(int, input().split())
t = list(map(int, input().split()))

ans = 0
for n in range(1, N):
    ans += min(T, t[n] - t[n-1])

print(ans+T)
