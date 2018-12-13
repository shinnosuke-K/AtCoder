# -*- coding: utf-8 -*-
def function(n):
    if n == 0:
        return 'P'
    else:
        burger = 'B' + function(n - 1) + 'P' + function(n - 1) + 'B'
        return burger


n, k = map(int, input().split())
burger = function(n)
print(burger[-1 * k::].count('P'))