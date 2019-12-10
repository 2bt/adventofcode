import math

s = set()
for y, r in enumerate(open("input")):
    for x, c in enumerate(r):
        if c == "#": s.add((x, y))

n, p = max((len(set(math.atan2(q[0] - p[0], q[1] - p[1]) for q in s if q != p)), p) for p in s)
print n

a = sorted(
    (-math.atan2(q[0] - p[0], q[1] - p[1]), abs(q[0] - p[0]) + abs(q[1] - p[1]), q)
    for q in s if q != p)
i = 0
for _ in range(200):
    q = a.pop(i)
    while q[0] == a[i%len(a)][0]: i = (i + 1) % len(a)
x, y = q[2]
print x * 100 + y

