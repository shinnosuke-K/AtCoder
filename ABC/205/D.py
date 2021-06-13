_, q = map(int, input().split(" "))
a = list(map(int, input().split(" ")))

for _ in range(q):
    k = int(input())
    
    if max(a) < k:
        print(k + len(a))
        continue
    
    n = 0
    if k in a:
        n = a.index(k)
    
    while True:
        if not k in a:
            print(k+n)
            break
        k += 1