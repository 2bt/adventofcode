s = 0
bs = [[] for _ in range(256)]
for h in open("input").read().strip().split(","):
    x = 0
    for c in bytes(h, "ascii"):
        if c in (ord("="), ord("-")): y = x
        x += c
        x *= 17
        x &= 255
    s += x
    b = bs[y]
    if "-" in h:
        for i, (l, _) in enumerate(b):
            if l == h[:-1]: b.pop(i)
    else:
        e, f = h.split("=")
        for i, (l, _) in enumerate(b):
            if l == e:
                b[i] = (l, f)
                break
        else: b.append((e, f))
print(s, sum((i + 1) * sum((j + 1) * int(x) for j, (_, x) in enumerate(b)) for i, b in enumerate(bs)))
