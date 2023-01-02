import re
import math
A = {}
R = {"AA":0}
Q = set()
for l in open("input"):
    vs = re.findall("[A-Z][A-Z]", l)
    v = vs.pop(0)
    A[v] = {x:1 for x in vs}
    r = int(re.search(r"\d+", l)[0])
    if r:
        R[v] = r
        Q.add(v)
for v in R:
    a = A[v]
    a[v] = 0
    for x in A:
        if not x in a: a[x] = math.inf
    for _ in range(len(A) - 1):
        for u, b in A.items():
            for w, dist in b.items(): a[w] = min(a[w], a[u] + dist)

def f(o=tuple(Q), t=30, v="AA", r=0):
    if t == 0 or not o: return r * t
    p = 0
    for i, w in enumerate(o):
        dt = min(t, A[v][w] + 1)
        p = max(p, dt * r + f(o[:i] + o[i+1:], t - dt, w, r + R[w]))
    return p
print(f())

from itertools import chain, combinations
y = 0
for o in chain.from_iterable(combinations(Q, r) for r in range(7, len(Q) - 6)):
    y = max(y, f(o, 26) + f(tuple(Q - set(o)), 26))
print(y)
