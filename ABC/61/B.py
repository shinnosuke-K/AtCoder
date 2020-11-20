N, M = map(int, input().split())
route = [0 for _ in range(N)]

for n in range(M):
    a, b = map(int, input().split())
    route[a-1] += 1
    route[b-1] += 1

for n in route:
    print(n)