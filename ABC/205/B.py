n = int(input())
a = list(map(int, input().split(" ")))

for i in range(1, n + 1):
    if not i in a:
        print("No")
        exit(0)
print("Yes")