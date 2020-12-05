from math import sqrt
X = int(input())


def is_prime(X):
    if X == 2:
        return True

    for i in range(2, int(sqrt(X))+1):
        if X % i == 0:
            return False
    return True


if X % 2 == 0 and X != 2:
    X += 1

while True:
    if is_prime(X):
        print(X)
        break
    else:
        X += 2