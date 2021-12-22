import re

def carve(a, b):
    x1, x2, y1, y2, z1, z2 = a
    u1, u2, v1, v2, w1, w2 = b
    if x1 > u2 or x2 < u1 or y1 > v2 or y2 < v1 or z1 > w2 or z2 < w1: return [a]
    ss = []
    if x1 < u1 <= x2:
        ss.append((x1, u1 - 1, y1, y2, z1, z2))
        x1 = u1
    if x1 <= u2 < x2:
        ss.append((u2 + 1, x2, y1, y2, z1, z2))
        x2 = u2
    if y1 < v1 <= y2:
        ss.append((x1, x2, y1, v1 - 1, z1, z2))
        y1 = v1
    if y1 <= v2 < y2:
        ss.append((x1, x2, v2 + 1, y2, z1, z2))
        y2 = v2
    if z1 < w1 <= z2:
        ss.append((x1, x2, y1, y2, z1, w1 - 1))
        z1 = w1
    if z1 <= w2 < z2:
        ss.append((x1, x2, y1, y2, w2 + 1, z2))
        z2 = w2
    return ss

for n in 1, 2:
    s = []
    for l in open("input"):
        cmd, coords = l.split()
        b = tuple(map(int, re.findall("-?\d+", coords)))
        if n == 1:
            x1, x2, y1, y2, z1, z2 = b
            if x1 > 50 or x2 < -50 or y1 > 50 or y2 < -50 or z1 > 50 or z2 < -50: continue
        ss = []
        for a in s: ss += carve(a, b)
        s = ss
        if cmd == "on": s.append(b)
    print(sum((x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1) for x1, x2, y1, y2, z1, z2 in s))
