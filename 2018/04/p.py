import collections

a = collections.defaultdict(int)
b = collections.defaultdict(lambda:[0] * 60)
t1 = 0
for l in sorted(open("input")):
    d, t, c, n = l.split()[:4]
    t0, t1 = t1, 0 if t[:2] == "23" else int(t[3:5])
    if c == "Guard": g = int(n[1:])
    if c == "wakes":
        a[g] += t1 - t0
        for i in range(t0, t1): b[g][i] += 1

g = max(a, key=a.__getitem__)
print(g * max(range(60), key=b[g].__getitem__))

g = max(a, key=lambda g: max(b[g]))
print(g * max(range(60), key=b[g].__getitem__))
