import math
b = []
for y, l in enumerate(open("input")):
    for x, c in enumerate(l):
        d = ">v<^".find(c)
        if d >= 0: b.append((x - 1, y - 1, d))
W, H, _ = map(max, zip(*b))
W += 1
H += 1
T = []
for _ in range(math.lcm(W, H)):
    T.append({(x, y) for x, y, _ in b})
    b = [((x + [1,0,-1,0][d]) % W, (y + [0,1,0,-1][d]) % H, d) for x, y, d in b]
def f(orig, dst):
    q = [orig]
    v = set()
    while q:
        x, y, t = q.pop(0)
        tt = t + 1
        for xx, yy in (x,y), (x-1,y), (x+1,y), (x,y-1), (x,y+1):
            if (xx, yy) == dst:
                return tt
            if (xx, yy) in T[tt % len(T)]: continue
            if (xx, yy) != (x, y) and not (0 <= xx < W and 0 <= yy < H): continue
            if (xx, yy, tt % len(T)) not in v:
                v.add((xx, yy, tt % len(T)))
                q.append((xx, yy, tt))
t1 = f((0, -1, 0), (W-1, H))
t2 = f((W-1, H, t1), (0, -1))
t3 = f((0, -1, t2), (W-1, H))
print(t1, t3)
