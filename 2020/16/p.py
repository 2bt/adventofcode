import re

f = open("input")
r = []
while 1:
    l = f.readline().strip()
    if not l: break
    r.append(list(map(int, re.findall("[0-9]+", l))))
f.readline()
t = list(map(int, f.readline().split(",")))
f.readline()
f.readline()

e = 0
m = [set(range(len(t))) for _ in t]

for l in f:
    q = list(map(int, l.split(",")))
    for i, v in enumerate(q):
        valid = True
        for x, y, z, w in r:
            if x <= v <= y or z <= v <= w: break
        else:
            valid = False
            e += v
        if valid:
            for j, (x, y, z, w) in enumerate(r):
                if not (x <= v <= y or z <= v <= w): m[j].discard(i)
print(e)

s = set()
for x in sorted(m, key=len):
    u = x | s
    x -= s
    s = u

f = 1
for x in m[:6]: f *= t[min(x)]
print(f)
