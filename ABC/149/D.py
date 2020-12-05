N, K = map(int, input().split())
R, S, P = map(int, input().split())
T = list(input())

j = {
    "r": ["p", P],
    "s": ["r", R],
    "p": ["s", S],
}

score = 0
hand = ["" for _ in range(N)]
for i in range(len(T)):
    pl = j[T[i]]
    if i >= K:
        if hand[i-K] != pl[0]:
            score += pl[1]
            hand[i] = pl[0]
    else:
        score += pl[1]
        hand[i] = pl[0]
print(score)