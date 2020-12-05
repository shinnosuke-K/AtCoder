A, B, K = map(int, input().split())
if A <= K:
    K = K - A
    A = 0
else:
    A = A - K
    K = 0

if B <= K:
    B = 0
else:
    B = B - K

print(A, B)