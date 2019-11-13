import math
for x in range(1, 1001):
    if 1 <= x <= 6:
        print('{0}:{1}'.format(x, 1))
    elif 7 <= x <= 11:
        print('{0}:{1}'.format(x, 2))
    else:
        print('{0}:{1}'.format(x, math.ceil(round(x / 5.5, 1))))

# x = int(input())
# if 1 <= x <= 6:
#     print(1)
# elif 7 <= x <= 11:
#     print(2)
# else:
#     print((x // 11) * 2 + 1)
