import collections
d = collections.defaultdict(list)
e = collections.defaultdict(list)
for l in open("input"):
    k, v = l.split(" contain ")
    k, _ = k.rsplit(" ", 1)
    for v in v.split(", "):
        v = v.split()
        t = " ".join(v[1:3])
        d[t].append(k)
        if v[0].isdigit(): e[k].append((int(v[0]), t))

q = ["shiny gold"]
v = set()
while q:
    k = q.pop()
    v.add(k)
    for x in d[k]:
        if not x in v: q.append(x)
print(len(v) - 1)

def f(k): return 1 + sum(n * f(v) for n, v in e[k])
print(f("shiny gold") - 1)
