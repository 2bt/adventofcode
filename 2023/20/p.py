class Module:
    def __init__(self, t, o):
        self.t = t
        self.p = 0
        self.i = []
        self.o = o

ms = {}
for l in open("input"):
    n, cs = l[1:].strip().split(" -> ")
    ms[n] = Module(l[0], cs.split(", "))

for n, m in ms.items():
    for o in m.o:
        if o in ms: ms[o].i.append(n)

u = next(m.i for n, m in ms.items() if "rx" in m.o)
l = []
hp = 0
lp = 0
i = 0
while u:
    i += 1
    q = [("button", 0, "roadcaster")]
    while q:
        s, p, n = q.pop(0)
        hp += p
        lp += 1 ^ p
        if n not in ms: continue
        m = ms[n]
        if m.t == "%":
            if p == 0:
                m.p ^= 1
                for o in m.o: q.append((n, m.p, o))
        elif m.t == "&":
            m.p = 1 ^ all(ms[i].p for i in m.i)
            for o in m.o: q.append((n, m.p, o))
            if m.p == 1 and n in u:
                u.remove(n)
                l.append(i)
        else:
            m.p = p
            for o in m.o: q.append((n, m.p, o))
    if i == 1000: print(hp * lp)
import math
print(math.lcm(*l))
