import re, collections
bs = [tuple(map(int, re.findall(r"\d+", l))) for l in open("input")]
bs.sort(key=lambda b:b[2])

g = {}
below = collections.defaultdict(set)
above = collections.defaultdict(set)

for i, (x1, y1, z1, x2, y2, z2) in enumerate(bs):
    while z1 > 1:
        found = False
        for x in range(x1, x2+1):
            for y in range(y1, y2+1):
                p = (x, y, z1-1)
                if p in g:
                    below[i].add(g[p])
                    above[g[p]].add(i)
                    found = True
        if found: break
        z1 -= 1
        z2 -= 1
    for x in range(x1, x2+1):
        for y in range(y1, y2+1):
            for z in range(z1, z2+1):
                g[x, y, z] = i

s1 = s2 = 0
for i in range(len(bs)):
    s1 += all(below[a] - {i} for a in above[i])

    q = [i]
    v = {i}
    while q:
        n = q.pop(0)
        for a in above[n]:
            if a in v: continue
            if not below[a] - v:
                v.add(a)
                q.append(a)
    s2 += len(v) - 1

print(s1, s2)
