q = open("input").read().strip().split("\n\n")
seeds = list(map(int, q.pop(0).split()[1:]))
maps = [[list(map(int, l.split())) for l in d.split("\n")[1:]] for d in q]
s = set(seeds)
for m in maps:
    z, s = s, set()
    v = set()
    for a, b, c in m:
        for x in z:
            if x >= b and x < b + c:
                s.add(x - b + a)
                v.add(x)
    s |= z - v
print(min(s))
s = [seeds[i : i + 2] for i in range(0, len(seeds), 2)]
for m in maps:
    z = []
    while s:
        x, y = s.pop()
        for a, b, c in m:
            if x + y <= b:
                continue
            if x < b and x + y > b:
                s.append([x, b - x])
                y -= b - x
                x = b
            if x < b + c and x + y > b + c:
                s.append([b + c, x + y - (b + c)])
                y = b + c - x
            if x >= b and x + y <= b + c:
                z.append([x - b + a, y])
                break
        else:
            z.append([x, y])
    s = z
print(min(s)[0])
