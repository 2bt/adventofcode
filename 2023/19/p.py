W, P = open("input").read().split("\n\n")
ws = {}
for w in W.split():
    n, rs = w.split("{")
    rr = []
    for r in rs[:-1].split(","):
        if ":" in r:
            r, tw = r.split(":")
            rr.append(("xmas".find(r[0]), r[1], int(r[2:]), tw))
        else:
            rr.append((r,))
    ws[n] = rr

s = 0
for p in P.split():
    t = tuple(int(x[2:]) for x in p[1:-1].split(","))
    n = "in"
    while n not in "RA":
        for r in ws[n]:
            if len(r) == 1:
                n = r[0]
                break
            if (r[1] == "<" and t[r[0]] < r[2] or
                r[1] == ">" and t[r[0]] > r[2]):
                n = r[3]
                break
    if n == "A": s += sum(t)
print(s)


def f(n, bounds):
    if n == "R": return 0
    if n == "A":
        s = 1
        for x, y in bounds:
            assert x <= y
            s *= y - x + 1
        return s

    s = 0
    bounds = bounds*1
    for r in ws[n]:
        if len(r) == 1: return s + f(r[0], bounds)
        i, o, v, w = r
        b = bounds[i]
        if o == "<":
            if b[1] < v: return s + f(w, bounds)
            if b[0] <= v - 1:
                bounds[i] = (b[0], v - 1)
                s += f(w, bounds)
                bounds[i] = (v, b[1])
        else:
            if b[0] > v: return s + f(w, bounds)
            if b[1] >= v + 1:
                bounds[i] = (v + 1, b[1])
                s += f(w, bounds)
                bounds[i] = (b[0], v)


print(f("in", [(1, 4000)] * 4))
