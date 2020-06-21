n = int(input())

ans = ''
while n > 26:
    n, mod = divmod(n-1, 26)
    ans += chr(ord('a') + mod)


ans += chr(ord('a') + (n-1) % 26)
print(ans[::-1])