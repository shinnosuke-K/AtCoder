n = int(input())
a = list(map(int, input().split()))
now_a = a[0]
count = 0

'''
True = positive
False = negative
'''
sign = True
if now_a < 0:
    sign = False

for i in range(1, n):
    next_a = now_a + a[i]
    if sign:
        if next_a >= 0:
            count += next_a + 1
            now_a = -1
        else:
            now_a = next_a
        sign = False
    else:
        if next_a <= 0:
            count += abs(next_a) + 1
            now_a = 1
        else:
            now_a = next_a
        sign = True
print(count)
