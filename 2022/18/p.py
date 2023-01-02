g = set(tuple(map(int, l.split(","))) for l in open("input"))

def neighbors(x, y, z):
    return [(x + 1, y, z), (x - 1, y, z),
            (x, y + 1, z), (x, y - 1, z),
            (x, y, z + 1), (x, y, z - 1)]

print(sum(n not in g for c in g for n in neighbors(*c)))

o = 0
q = [(-1, -1, -1)]
v = set()
while q:
    c = q.pop(0)
    for n in neighbors(*c):
        if n in g: o += 1
        elif n not in v and all(-1 <= x <= 22 for x in n):
            v.add(n)
            q.append(n)
print(o)
