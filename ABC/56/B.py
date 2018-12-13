# -*- coding: utf-8 -*-
w, a, b = map(int, input().split())
ax = [a + x for x in range(w + 1)]
bx = [b + x for x in range(w + 1)]
if a > b:
    print(ax[0] - bx[-1] if ax[0] - bx[-1] >= 0 else 0)
elif a < b:
    print(bx[0] - ax[-1] if bx[0] - ax[-1] >= 0 else 0)
else:
    print(0)