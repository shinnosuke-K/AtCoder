A, B, X = map(int, input().split())
high = 10**9+1
low = 0
mid = 0
while high - low > 1:
    mid = (high + low) // 2
    if A*mid + B*len(str(mid)) > X:
        high = mid
    else:
        low = mid
print(low)