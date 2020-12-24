import re, collections

d = {
    "w":  (-1, 1, 0),
    "e":  (1, -1, 0),
    "sw": (-1, 0, 1),
    "ne": (1, 0, -1),
    "nw": (0, 1, -1),
    "se": (0, -1, 1),
}

g = set()
for l in open("input"):
    p = 0, 0, 0
    for t in re.findall("e|se|sw|w|nw|ne", l):
        u, v, w = d[t]
        x, y, z = p
        p = x + u, y + v, z + w
    if p in g: g.remove(p)
    else: g.add(p)
print(len(g))

for _ in range(100):
    n = collections.defaultdict(int)
    for x, y, z in g:
        for u, v, w in d.values(): n[x + u, y + v, z + w] += 1
    g = {p for p, c in n.items() if [c == 2, 0 < c < 3][p in g]}
print(len(g))
