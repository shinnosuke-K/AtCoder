n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a.sort()
b.sort()

sub = [b[i] - a[i] for i in range(n)]

if -1 in sub:
    print('No')
else:
    print('Yes')