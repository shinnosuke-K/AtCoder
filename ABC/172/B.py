s = list(input())
t = list(input())
count = 0
for n in range(len(s)):
    if s[n] != t[n]:
        count += 1
print(count)