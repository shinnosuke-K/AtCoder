
n = int(input())
h = int(input())
w = int(input())
count = 0
a = 0
for i in range(n - h + 1):
    for j in range(n // w):
        for k in range(n // w):
            if w + w * k + j <= n and h + i <= n:
                count += 1


print(count)
