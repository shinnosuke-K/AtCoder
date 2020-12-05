N = int(input())
a = list(map(int, input().split()))
count = 0
n = 1
flag = False
for i in range(N):
    if a[i] == n:
        n += 1
        flag = True
    else:
        count += 1

if flag:
    print(count)
else:
    print(-1)
