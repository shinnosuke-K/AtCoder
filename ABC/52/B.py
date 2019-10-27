n = int(input())
s = list(input())
ans = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    if s[i - 1] == "I":
        ans[i] = ans[i - 1] + 1
    else:
        ans[i] = ans[i - 1] - 1

print(max(ans))

# other answer
n = int(input())
s = input()

ans = 0
now = 0
for i in s:
    if i == 'I':
        now += 1
    else:
        now -= 1
    ans = max(ans, now)

print(ans)