import math

def main():
    a, r, n = map(int, input().split())
    if math.log10(a) + (n-1)*math.log10(r) > 9:
        print("large")
    else:
        print(a * r**(n-1))


if __name__ == '__main__':
    main()
