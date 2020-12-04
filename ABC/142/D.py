import collections
A, B = map(int, input().split())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


ca = collections.Counter(prime_factorize(A))
cb = collections.Counter(prime_factorize(B))

count = 1
for c in ca.keys():
    if c in cb.keys():
        count += 1
print(count)