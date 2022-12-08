g = [list(map(int, l.strip())) for l in open("input")]
W, H = len(g[0]), len(g)

def count():
    for x in range(9999999): yield x
q = [[count() for x in l]for l in g]
p = set()
for _ in range(4):
    for r, s in zip(g, q):
        h = -1
        for x, i in zip(r, s):
            if x > h:
                p.add(i)
                h = x
    g = list(zip(*g[::-1]))
    q = list(zip(*q[::-1]))
print(len(p))

def get_score(x, y):
    h = g[y][x]
    d1 = d2 = d3 = d4 = 1
    while y + d1 < H-1 and g[y + d1][x] < h: d1 += 1
    while y - d2 > 0   and g[y - d2][x] < h: d2 += 1
    while x + d3 < W-1 and g[y][x + d3] < h: d3 += 1
    while x - d4 > 0   and g[y][x - d4] < h: d4 += 1
    return d1 * d2 * d3 * d4
s = 0
for y in range(1, H - 1):
    for x in range(1, W - 1):
        s = max(s, get_score(x, y))
print(s)
