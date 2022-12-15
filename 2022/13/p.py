import functools
def c(l, r):
    if type(l) == list:
        if type(r) != list: r = [r]
        for x, y in zip(l, r):
            q = c(x, y)
            if q != 0: return q
        return len(l) - len(r)
    if type(r) == list: return c([l], r)
    return l - r
s = 0
p = [[[2]], [[6]]]
d, e = p
for i, m in enumerate(open("input").read().split("\n\n")):
    l, r = map(eval, m.strip().split("\n"))
    if c(l, r) <= 0: s += i + 1
    p += [l, r]
print(s)
p.sort(key=functools.cmp_to_key(c))
print((p.index(d) + 1) * (p.index(e) + 1))
