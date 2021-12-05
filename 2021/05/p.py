import collections
for i in 1, 0:
    g = collections.defaultdict(int)
    for l in open("input"):
        x1, y1, x2, y2 = map(int, l.replace("->", ",").split(","))
        if i and x1 != x2 and y1 != y2: continue
        dx = (x1 < x2) - (x1 > x2)
        dy = (y1 < y2) - (y1 > y2)
        g[x1, y1] += 1
        while x1 != x2 or y1 != y2:
            x1 += dx
            y1 += dy
            g[x1, y1] += 1
    print(sum(x > 1 for x in g.values()))
