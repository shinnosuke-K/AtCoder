a, b, c = map(int, input().split())

i = 0
mod = []
while True:
    if a * i % b == c:
        print("YES")
        break
    elif a * i % b in mod:
        print("NO")
        break
    else:
        mod.append(a * i % b)
        i += 1
