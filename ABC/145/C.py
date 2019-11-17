import math
n = int(input())
c = [list(map(int, input().split())) for i in range(n)]
dis = 0
for i in range(n):
    for j in range(n):
        if j == i:
            continue
        else:
            dis += math.sqrt((c[i][0] - c[j][0])**2 + (c[i][1] - c[j][1])**2)

print(dis / n)
