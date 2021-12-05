a = [l.strip() for l in open("input")]

b = [c.count("1") > len(a) / 2 for c in zip(*a)]
g = sum( x      << i for i, x in enumerate(b[::-1]))
e = sum((1 - x) << i for i, x in enumerate(b[::-1]))
print(g * e)

def f(a, c):
    p = 0
    while len(a) > 1:
        s = sum(w[p] == "1" for w in a)
        keep = "01"[(s >= len(a) / 2) ^ c]
        a = [w for w in a if w[p] == keep]
        p += 1
    return int(a[0], 2)

print(f(a, 0) * f(a, 1))
