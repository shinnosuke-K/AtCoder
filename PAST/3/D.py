n0 = [
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", ".", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"]
      ]
n1 = [
        [".", "#", "."],
        ["#", "#", "."],
        [".", "#", "."],
        [".", "#", "."],
        ["#", "#", "#"]
      ]
n2 = [
        ["#", "#", "#"],
        [".", ".", "#"],
        ["#", "#", "#"],
        ["#", ".", "."],
        ["#", "#", "#"]
      ]
n3 = [
        ["#", "#", "#"],
        [".", ".", "#"],
        ["#", "#", "#"],
        [".", ".", "#"],
        ["#", "#", "#"]
      ]
n4 = [
        ["#", ".", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"],
        [".", ".", "#"],
        [".", ".", "#"]
      ]
n5 = [
        ["#", "#", "#"],
        ["#", ".", "."],
        ["#", "#", "#"],
        [".", ".", "#"],
        ["#", "#", "#"]
      ]
n6 = [
        ["#", "#", "#"],
        ["#", ".", "."],
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"]
      ]
n7 = [
        ["#", "#", "#"],
        [".", ".", "#"],
        [".", ".", "#"],
        [".", ".", "#"],
        [".", ".", "#"]
      ]
n8 = [
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"]
      ]
n9 = [
        ["#", "#", "#"],
        ["#", ".", "#"],
        ["#", "#", "#"],
        [".", ".", "#"],
        ["#", "#", "#"]
      ]
num_list = [n0, n1, n2, n3, n4, n5, n6, n7, n8, n9]


def main():
    N = int(input())
    s = [list(input()) for _ in range(5)]

    for i in range(N):
        num = []
        for j in range(5):
            num.append(s[j][4*(i+1)-3:4*(i+1)])

        i = 0
        for n in num_list:
            if num == n:
                print(i)
            else:
                i += 1


if __name__ == '__main__':
    main()
