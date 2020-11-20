N, K = map(int, input().split())
i = [[i+1, 0] for i in range(10**5)]

for n in range(N):
    a, b = map(int, input().split())
    i[a-1][1] += b

count = 0
for j in i:
    count += j[1]
    if count >= K:
        print(j[0])
        break
