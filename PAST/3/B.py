def main():
    n, m, q = map(int, input().split())

    h = [[] for _ in range(n)]

    slv = {}
    for i in range(m):
        slv[i+1] = n

    for _ in range(q):
        s = list(map(int, input().split()))

        if s[0] == 2:
            h[s[1] - 1].append(s[2])
            slv[s[2]] -= 1

        elif s[0] == 1:
            score = 0
            for i in h[s[1]-1]:
                score += slv[i]

            print(score)


if __name__ == '__main__':
    main()
