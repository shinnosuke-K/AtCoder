N = int(input())
if N % 2 != 0:
    print(0)
else:
    ans = 0
    n = 1
    while (10*n) <= N:
        ans += N // (10*n)
        n *= 5
    print(ans)