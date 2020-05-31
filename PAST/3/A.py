def main():
    s = input()
    t = input()

    if s == t:
        print("same")
    elif s.upper() == t or s == t.upper() or s.upper() == t.upper():
        print("case-insensitive")
    else:
        print("different")


if __name__ == '__main__':
    main()
