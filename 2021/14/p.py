from collections import defaultdict

f = open("input")
a = f.readline().strip()
f.readline()
r = {l[:2] : l[6] for l in f}

p = defaultdict(int)
for x, y in zip(a, a[1:]): p[x + y] += 1

for n in 10, 30:
    for _ in range(n):
        d = defaultdict(int)
        for k, v in p.items():
            if k in r:
                d[k[0] + r[k]] += v
                d[r[k] + k[1]] += v
            else: d[k] = v
        p = d
    c = defaultdict(int)
    for k, v in p.items(): c[k[0]] += v
    c[a[-1]] += 1
    print(max(c.values()) - min(c.values()))
