xs = []
ys = []
for l in open("input"):
    x, y = map(int, l.split(","))
    xs.append(x)
    ys.append(y)

x0, x1 = min(xs), max(xs)
y0, y1 = min(ys), max(ys)

g = [0] * len(xs)
b = [1] * len(xs)
q = 0
for y in range(y0, y1 + 1):
    for x in range(x0, x1 + 1):
        d = 999
        td = 0
        for i, (u, v) in enumerate(zip(xs, ys)):
            dd = abs(u - x) + abs(v - y)
            td += dd
            if dd == d: j = -1
            if dd < d: d = dd; j = i
        if j > -1:
            g[j] += 1
            if x in (x0, x1) or y in (y0, y1): b[j] = 0
        q += td < 10000
print(max(x * y for x, y in zip(b, g)))
print(q)
