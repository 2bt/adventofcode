jet = open("input").read().strip()
stones = [
    [27, 28, 29, 30],
    [12, 19, 20, 21, 28],
    [13, 21, 27, 28, 29],
    [3, 11, 19, 27],
    [19, 20, 27, 28],
]
g = bytearray(b"#" * 8)
j = 0
J = {}
N = 1000000000000
i = 0
eh = 0
while i < N:
    while not g.startswith(b"#......." * 7): g[:0] = b"#......."
    s = stones[i % len(stones)]
    while 1:
        dx = jet[j] == ">" or -1
        j = (j + 1) % len(jet)
        t = [x + dx for x in s]
        if all(g[x] == ord('.') for x in t): s = t
        t = [x + 8 for x in s]
        if not all(g[x] == ord('.') for x in t): break
        s = t
    for x in s: g[x] = ord('@')
    while g.startswith(b"#......."): del g[:8]
    h = len(g) // 8 - 1
    if i == 2021: print(h)
    if i > 2021 and eh == 0:
        if j in J:
            ii, hh = J[j]
            if ii % len(stones) == i % len(stones):
                di = i - ii
                x = (N - i) // di
                i += di * x
                eh = (h - hh) * x
        J[j] = (i, h)
    i += 1
print(h + eh)
