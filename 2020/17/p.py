import collections

g = { (x, y, 0) for y, l in enumerate(open("input")) for x, c in enumerate(l) if c == "#" }
for _ in range(6):
    a = collections.defaultdict(int)
    for x, y, z in g:
        for u in range(x - 1, x + 2):
            for v in range(y - 1, y + 2):
                for s in range(z - 1, z + 2): a[u, v, s] += 1
    g = {k for k, v in a.items() if [v == 3, 3 <= v <= 4][k in g]}
print(len(g))

g = { (x, y, 0, 0) for y, l in enumerate(open("input")) for x, c in enumerate(l) if c == "#" }
for _ in range(6):
    a = collections.defaultdict(int)
    for x, y, z, w in g:
        for u in range(x - 1, x + 2):
            for v in range(y - 1, y + 2):
                for s in range(z - 1, z + 2):
                    for t in range(w - 1, w + 2): a[u, v, s, t] += 1
    g = {k for k, v in a.items() if [v == 3, 3 <= v <= 4][k in g]}
print(len(g))
