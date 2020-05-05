o = input()
e = input()
p = ''
i, j = 0, 0
for n in range(len(o) + len(e)):
    if n % 2 != 0:
        p += e[i]
        i += 1
    else:
        p += o[j]
        j += 1

print(p)