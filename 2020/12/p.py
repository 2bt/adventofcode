x = y = d = 0
for l in open("input"):
    c, v = l[0], int(l[1:])
    if c == "N": y -= v
    if c == "S": y += v
    if c == "W": x -= v
    if c == "E": x += v
    if c == "R": d += v // 90
    if c == "L": d -= v // 90
    if c == "F":
        x += [1, 0, -1, 0][d % 4] * v
        y += [0, 1, 0, -1][d % 4] * v
print(abs(x) + abs(y))


x = 10
y = -1
px = py = 0
for l in open("input"):
    c, v = l[0], int(l[1:])
    if c == "N": y -= v
    if c == "S": y += v
    if c == "W": x -= v
    if c == "E": x += v
    if c in "RL":
        if c == "L": v = -v
        for _ in range(v // 90 % 4): x, y = -y, x
    if c == "F":
        px += x * v
        py += y * v
print(abs(px) + abs(py))
