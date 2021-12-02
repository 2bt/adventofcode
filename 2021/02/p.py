d = 0
h = 0
for l in open("input"):
    c, v = l.split()
    v = int(v)
    if c == "forward": h += v
    if c == "down":    d += v
    if c == "up":      d -= v
print(d * h)


d = 0
h = 0
a = 0
for l in open("input"):
    c, v = l.split()
    v = int(v)
    if c == "forward": h += v; d += a * v
    if c == "down":    a += v
    if c == "up":      a -= v
print(d * h)
