import collections

r = {}
for l in open("input"):
    a, b = l.strip().split(" => ")
    a = [(int(w.split()[0]), w.split()[1]) for w in a.split(", ")]
    n, k = int(b.split()[0]), b.split()[1]
    r[k] = [n, a]

def d(k, q = {"ORE":0}):
    if k in q: return q[k]
    return 1 + max(d(a) for _, a in r[k][1])

def f(n):
    s = collections.defaultdict(int)
    s ["FUEL"] = n
    while 1:
        k = max(s.keys(), key=d)
        if k == "ORE": break
        n, a = r[k]
        f = (s[k] + n - 1) / n
        del s[k]
        for x, q in a: s[q] += x * f
    return s["ORE"]

print f(1)
a = 1
b = 5000000
t = 1000000000000
while 1:
    c = (a + b + 1) / 2
    o = f(c)
    if o < t: a = c
    if o > t: b = c
    if a + 1 == b: break
print a
