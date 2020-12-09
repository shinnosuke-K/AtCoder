import itertools

N = int(input())
P = int("".join(input().split()))
Q = int("".join(input().split()))

t = [i+1 for i in range(N)]
l = list(itertools.permutations(t))

cp = 0
cq = 0
for i in range(len(l)):
    if P == int("".join(map(str, l[i]))):
        cp = i

    if Q == int("".join(map(str, l[i]))):
        cq = i

    if cp != 0 and cq != 0:
        break
print(abs(cp - cq))