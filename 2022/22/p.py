import re
R = 50
W = 4 * R
g, c = open("input").read().split("\n\n")
a = [l.ljust(W) for l in g.splitlines() + [""]]
"""
.12.
.5..
89..
c...
"""
for Q in {
    (2,0): (1,0),
    (1,2): (2,2),
    (5,0): (5,0),
    (5,2): (5,2),
    (9,0): (8,0),
    (8,2): (9,2),
    (12,0): (12,0),
    (12,2): (12,2),
    (12,1): (8,1),
    (8,3): (12,3),
    (9,1): (1,1),
    (1,3): (9,3),
    (2,1): (2,1),
    (2,3): (2,3),
}, {
    (1,2): (8,0),
    (8,2): (1,0),
    (1,3): (12,0),
    (12,2): (1,1),
    (2,0): (9,2),
    (9,0): (2,2),
    (2,1): (5,2),
    (5,0): (2,3),
    (2,3): (12,3),
    (12,1): (2,1),
    (5,2): (8,1),
    (8,3): (5,0),
    (9,1): (12,2),
    (12,0): (9,3),
}:
    x = g.find(".")
    x = R
    y = 0
    d = 0
    for w in re.findall("\d+|.", c):
        if w in "RL":
            d = (d + [-1,1][w == "R"]) % 4
            continue
        for _ in range(int(w)):
            xx, yy = x, y
            if d == 0: xx += 1
            if d == 1: yy += 1
            if d == 2: xx -= 1
            if d == 3: yy -= 1
            dd = d
            if a[yy][xx] == " ":
                i, f = Q[y//R*4 + x//R, d]
                xx %= R
                yy %= R
                while dd != f:
                    dd = (dd + 1) % 4
                    xx, yy = R - yy - 1, xx
                xx += i%4*R
                yy += i//4*R
            if a[yy][xx] == "#": break
            x = xx
            y = yy
            d = dd
    print((y + 1) * 1000 + (x + 1) * 4 + d)