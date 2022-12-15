def clamp(v, a, b): return max(a, min(b, v))
g = set()
for l in open("input"):
    x = y = None
    for xy in l.strip().split(" -> "):
        tx, ty = map(int, xy.split(","))
        if x == None: x, y = tx, ty
        g.add((tx, ty))
        while x != tx or y != ty:
            x = clamp(tx, x - 1, x + 1)
            y = clamp(ty, y - 1, y + 1)
            g.add((x, y))
Y = max(y for x, y in g)
s1 = False
for i in range(99999):
    x, y = 500, 0
    if (x, y) in g:
        print(i)
        break
    while 1:
        if y > Y:
            if not s1:
                print(i)
                s1 = True
            g.add((x, y))
            break
        if (x, y + 1) not in g:
            y += 1
        elif (x - 1, y + 1) not in g:
            x -= 1
            y += 1
        elif (x + 1, y + 1) not in g:
            x += 1
            y += 1
        else:
            g.add((x, y))
            break
