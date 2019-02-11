num = [1, 4, 7, 9]
n = list(map(int, input().split()))
n.sort()
if num == n:
    print('YES')
else:
    print('NO')