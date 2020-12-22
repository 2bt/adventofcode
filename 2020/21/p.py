import functools

allergens = set()
foods     = []

for l in open("input"):
    x, y = l.split(" (contains ")
    x = set(x.split())
    y = set(y[:-2].split(", "))
    foods.append((x, y))
    allergens |= y

d = {}
p = set()
for a in allergens:
    s = None
    for x, y in foods:
        if a in y:
            if s is None: s = set(x)
            s &= x
    d[a] = s
    p |= s

c = 0
for x, y in foods: c += len(x - p)
print(c)

l = []
while d:
    a = min(d, key=lambda a: len(d[a]))
    i = min(d[a])
    del d[a]
    for s in d.values(): s.discard(i)
    l.append((a, i))
print(",".join(y for x, y in sorted(l)))
