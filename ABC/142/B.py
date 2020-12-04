N, K = map(int, input().split())
h = list(map(int, input().split()))
count = 0
for i in range(len(h)):
    if h[i] >= K:
        count += 1
print(count)