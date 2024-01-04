x = y = 0
X = Y = 0
z = []
Z = []
p = P = 2
for l in open("input"):
    z.append((x, y))
    d, l, c = l.split()
    l = int(l)
    x += {"R": l, "L": -l}.get(d, 0)
    y += {"D": l, "U": -l}.get(d, 0)
    p += l
    Z.append((X, Y))
    l = int(c[2:7], 16)
    d = int(c[7])
    X += [l, 0, -l, 0][d]
    Y += [0, l, 0, -l][d]
    P += l
def f(z): return sum(x * v - y * u for (x, y), (u, v) in zip(z, z[1:] + [z[0]])) // 2
print(f(z) + p // 2, f(Z) + P // 2)
