
n = list(map(int, input().split()))

if n[0] * n[1] > n[2] * n[3]:
    print(n[0] * n[1])
else:
    print(n[2] * n[3])

# other
# n = list(map(int, input().split()))
# print(max(n[0]*n[1], n[2]*n[3]))
