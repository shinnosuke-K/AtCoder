import sys

n, m = map(int, input().split())
ab = [list(map(int, input().split())) for _ in range(n)]
cd = [list(map(int, input().split())) for _ in range(m)]

ans = [0 for _ in range(n)]

for i in range(n):
    dis = sys.maxsize
    for j in range(m):
        abs_dis = abs(ab[i][0] - cd[j][0]) + abs(ab[i][1] - cd[j][1])
        if dis > abs_dis:
            ans[i] = j + 1
            dis = abs_dis

for n in range(len(ans)):
    if n == len(ans) - 1:
        print(ans[n], end="")
    else:
        print(ans[n])
