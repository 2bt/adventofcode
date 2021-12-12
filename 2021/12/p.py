from collections import defaultdict

d = defaultdict(set)
for l in open("input"):
    a, b = l.strip().split("-")
    d[a].add(b)
    d[b].add(a)

def f(k, n="start", v=set()):
    if n in v:
        if n == "start" or k: return 0
        else: k = True
    if n == "end": return 1
    if n.islower(): v = v | {n}
    return sum(f(k, x, v) for x in d[n])

print(f(True))
print(f(False))
