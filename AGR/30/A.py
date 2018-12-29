# -*- coding: utf-8 -*-
a, b, c = map(int, input().split())
if a + b >= c:
    print(b + c)
else:
    print(a + b * 2 + 1)
