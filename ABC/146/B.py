N = int(input())
S = list(map(ord, input()))
ans = ""
for i in range(len(S)):
    if S[i]+N > ord("Z"):
        ans += chr(ord("A") + S[i]+N - ord("Z")-1)
    else:
        ans += chr(S[i]+N)
print(ans)