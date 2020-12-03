N = int(input())
s = [int(input()) for _ in range(N)]
s.sort()

if sum(s) % 10 != 0:
    print(sum(s))
else:
    for i in s:
        if i % 10 != 0:
            print(sum(s) - i)
            exit()
    else:
        print(0)
