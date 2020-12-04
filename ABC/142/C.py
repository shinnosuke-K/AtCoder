ans = ["" for _ in range(int(input()))]
A = list(map(int, input().split()))
for i in range(len(A)):
    ans[A[i] - 1] = str(i + 1)
print(" ".join(ans))
