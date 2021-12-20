f = open("input")
t = f.readline()
a = set((x, y) for y, l in enumerate(f) for x, c in enumerate(l) if c == "#")

for n in 2, 48:
    for i in range(n):
        b = set()
        for x, y in a:
            for v in range(-1, 2):
                for u in range(-1, 2): b.add((x + u, y + v))
        c = set()
        for x, y in b:
            o = 0
            for v in range(-1, 2):
                for u in range(-1, 2): o = o * 2 + ((x + u, y + v) in a)
            if i % 2:
                if t[o ^ 511] == "#": c.add((x, y))
            else:
                if t[o] == ".": c.add((x, y))
        a = c
    print(len(a))
