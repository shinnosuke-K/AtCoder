from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
a_dic = defaultdict(int)
for i in range(n):
    a_dic[a[i]] += 1

q = int(input())
for _ in range(q):
    b, c = map(int, input().split())

    a_dic[c] += a_dic[b]
    a_dic[b] = 0
    a_sum = 0
    for k, v in a_dic.items():
        a_sum += k * v

    print(a_sum)
