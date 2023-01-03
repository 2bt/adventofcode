import re
from functools import cache
s = 0
q = 1
for l in open("input"):
    i, oo, co, bo, bc, go, gb = map(int, re.findall(r"\d+", l))
    maxg = 0
    @cache
    def f(t, ro=1, rc=0, rb=0, o=0, c=0, b=0, g=0):
        if t == 0:
            global maxg
            maxg = max(maxg, g)
            return
        if g + t * (t - 1) // 2 <= maxg: return
        if o >= go and b >= gb:
            f(t-1, ro, rc, rb, o-go+ro, c+rc, b-gb+rb, g+t-1)
            return
        if o >= bo and c >= bc and rb < gb:
            f(t-1, ro, rc, rb+1, o-bo+ro, c-bc+rc, b+rb, g)
        if o >= co and rc < bc:
            f(t-1, ro, rc+1, rb, o-co+ro, c+rc, b+rb, g)
        if o >= oo and ro < max(oo, co, bo, go):
            f(t-1, ro+1, rc, rb, o-oo+ro, c+rc, b+rb, g)
        f(t-1, ro, rc, rb, o+ro, c+rc, b+rb, g)
    f(24)
    s += i * maxg
    if i <= 3:
        f(32)
        q *= maxg
print(s)
print(q)
