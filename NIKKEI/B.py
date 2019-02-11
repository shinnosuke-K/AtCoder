n = int(input())
a = input()
b = input()
c = input()
count_1 = 0
count_2 = 0
count_3 = 0
for i in range(n):
    if a[i] == b[i]:
        count_1 += 1
    if a[i] == c[i]:
        count_2 += 1
    if b[i] == c[i]:
        count_3 += 1

