a = open("input").read()
W = a.find("\n") + 1
H = W - 1
c = set()
r = set()
for i in range(H):
    if "#" not in a[i*W:i*W+H]: r.add(i)
    if "#" not in a[i::W]: c.add(i)
ps = [(i%W, i//W)  for i, c in enumerate(a) if c == "#"]
for F in 1, 999999:
    s = 0
    for i in range(len(ps)):
        for j in range(i + 1, len(ps)):
            x, y = ps[i]
            u, v = ps[j]
            if x > u: x, u = u, x
            if y > v: y, v = v, y
            s += u - x + v - y
            s += (len(c & set(range(x, u))) + len(r & set(range(y, v)))) * F
    print(s)
