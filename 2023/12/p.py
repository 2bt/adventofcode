from functools import cache
@cache
def f(r, d):
    if not d: return "#" not in r
    s = 0
    x = d[0]
    while 1:
        r = r.lstrip(".")
        q = r[:x]
        if len(q) == x and "." not in q and r[x:x+1] != "#":
            s += f(r[x + 1:], d[1:])
        if r[:1] != "?": return s
        r = r[1:]
s1 = s2 = 0
for l in open("input"):
    r, d = l.split()
    d = tuple(map(int, d.split(",")))
    s1 += f(r, d)
    s2 += f("?".join([r] * 5), d * 5)
print(s1, s2)
