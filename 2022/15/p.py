import re
def add_range(r, a, b):
    for i, (c, d) in enumerate(r):
        if b < c - 1:
            r.insert(i, (a, b))
            return
        if a > d + 1: continue
        a = min(a, c)
        b = max(b, d)
        while len(r) > i + 1 and r[i + 1][0] <= b:
            _, d = r.pop(i + 1)
            b = max(b, d)
        r[i] = (a, b)
        return
    r.append((a, b))
Y = 2000000
r = []
bb = set()
ss = []
for l in open("input"):
    sx, sy, bx, by = map(int, re.findall("-?\d+", l))
    d = abs(sx - bx) + abs(sy - by)
    ss.append((sx, sy, d))
    d -= abs(sy - Y)
    if d < 0: continue
    if by == Y: bb.add(bx)
    add_range(r, sx - d, sx + d)
print(sum(b - a + 1 for a, b in r) - len(bb))
Y = 4000000
for y in range(Y):
    r = []
    for sx, sy, d in ss:
        d -= abs(sy - y)
        if d < 0: continue
        add_range(r, sx - d, sx + d)
    if len(r) > 1: print((r[0][1] + 1) * Y + y)
