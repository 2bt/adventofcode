import collections
s1 = s2 = 0
for i, l in enumerate(open("input")):
    _, g = l.split(":")
    b = True
    cr = cb = cg = 0
    for r in g.split(";"):
        for p in r.split(","):
            n, c = p.split()
            n, c = int(n), c[0]
            if (c == "r" and n > 12 or
                c == "g" and n > 13 or
                c == "b" and n > 14): b = False
            if c == "r": cr = max(cr, n)
            if c == "g": cg = max(cg, n)
            if c == "b": cb = max(cb, n)
    if b: s1 += i + 1
    s2 += cr * cb * cg
print(s1, s2)
