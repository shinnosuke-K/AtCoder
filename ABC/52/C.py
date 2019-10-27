import math
from collections import defaultdict


def make_prime_list(num):
    if num < 2:
        return []

    # 0のものは素数じゃないとする
    prime_list = [i for i in range(num + 1)]
    prime_list[1] = 0 # 1は素数ではない
    num_sqrt = math.sqrt(num)

    for prime in prime_list:
        if prime == 0:
            continue
        if prime > num_sqrt:
            break

        for non_prime in range(2 * prime, num+1, prime):
            prime_list[non_prime] = 0

    return [prime for prime in prime_list if prime != 0]


num = int(input())
div_sum = defaultdict(int)

p = make_prime_list(num)
for j in range(2, num+1):

    div_num = defaultdict(int)

    for i in p:
        n = j
        while n % i == 0:
            div_num[i] += 1
            n //= i

    for k, v in div_num.items():
        div_sum[k] += v

ans = 1
for k, v in div_sum.items():
    ans *= (v + 1)
print(ans % (10**9 + 7))


def sample(x):
    i = 2
    count = 0
    while x % i == 0:
        count += 1
        x //= i
    print(count)


sample(math.factorial(1000))

# other answer
N = int(input())
M = 10 ** 9 + 7

factor = {}

for n in range(2, N + 1):
    p = 2
    root_n = math.sqrt(n)

    while n > 1 and p <= root_n:
        if n % p == 0:
            if p not in factor:
                factor[p] = 0

            while n % p == 0:
                n //= p
                factor[p] += 1

        p += 1

    if n > 1:
        if n not in factor:
            factor[n] = 1
        else:
            factor[n] += 1

print(factor)
#
ans = 1

for v in factor.values():
    ans *= (v + 1)

ans %= M

print(ans)