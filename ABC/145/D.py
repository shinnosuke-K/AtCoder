def cmb(n, r, mod):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r)
    return g1[n] * g2[r] * g2[n - r] % mod


# 出力の制限
mod = 10 ** 9 + 7
N = 10 ** 6

# 元テーブル
g1 = [1, 1]

# 逆元テーブル
g2 = [1, 1]

# 逆元テーブル計算用テーブル
inverse = [0, 1]

for i in range(2, N + 1):
    g1.append((g1[-1] * i) % mod)
    inverse.append((-inverse[mod % i] * (mod // i)) % mod)
    g2.append((g2[-1] * inverse[-1]) % mod)

x, y = map(int, input().split())
if (x + y) % 3 == 0:
    n = (x + y) // 3
    k = x - n
    print(cmb(n, k, mod) % (10 ** 9 + 7))
else:
    print(0)
