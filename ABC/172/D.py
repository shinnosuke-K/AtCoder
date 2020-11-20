n = int(input())
s = 0
for i in range(1, n + 1):
  d = n // i
  s += d * (d + 1) // 2 * i
print(s)