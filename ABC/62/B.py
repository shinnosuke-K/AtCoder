H, W = map(int, input().split())
a = [input() for _ in range(H)]

print("".join(["#" for _ in range(W+2)]))
for n in range(H):
    print("#" + a[n] + "#")
print("".join(["#" for _ in range(W+2)]))
