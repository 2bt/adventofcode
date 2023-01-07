from collections import defaultdict
a = set()
for y, l in enumerate(open("input")):
    for x, c in enumerate(l):
        if c == "#": a.add((x, y))
for i in range(1000):
    if i == 10:
        minx, miny = map(min, zip(*a))
        maxx, maxy = map(max, zip(*a))
        print((maxx - minx + 1) * (maxy - miny + 1) - len(a))
    p = {}
    c = defaultdict(int)
    for x, y in a:
        px = x
        py = y
        if sum((x + dx, y + dy) in a for dx in [-1, 0, 1] for dy in [-1, 0, 1]) > 1:
            for j in range(4):
                d = "NSWE"[(j + i) % 4]
                if   d == "N" and all((x+o, y-1) not in a for o in [-1, 0, 1]): py -= 1; break
                elif d == "S" and all((x+o, y+1) not in a for o in [-1, 0, 1]): py += 1; break
                elif d == "W" and all((x-1, y+o) not in a for o in [-1, 0, 1]): px -= 1; break
                elif d == "E" and all((x+1, y+o) not in a for o in [-1, 0, 1]): px += 1; break
        p[x, y] = px, py
        c[px, py] += 1
    b = set()
    for x, y in a:
        px, py = p[x, y]
        if c[px, py] <= 1: x, y = px, py
        b.add((x, y))
    if a == b:
        print(i + 1)
        break
    a = b
