# -*- coding: utf-8 -*-
n = int(input())
b = [1 / i for i in list(map(int, input().split()))]
print(1 / sum(b))