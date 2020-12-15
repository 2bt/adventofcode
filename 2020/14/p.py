m1 = {}
m2 = {}
for l in open("input"):
    q, v = l.strip().split(" = ")
    if q.startswith("mask"): mask = v[::-1]
    else:
        x = 0
        v = int(v)
        for i, b in enumerate(mask):
            if b == "1" or (b == "X" and (1 << i) & v): x |= 1 << i
        m1[int(q[4:-1])] = x

        a = int(q[4:-1])
        q = [0]
        for i, b in enumerate(mask):
            if b == "1" or (b == "0" and (1 << i) & a): q = [x | (1 << i) for x in q]
            if b == "X": q += [x | (1 << i) for x in q]
        for x in q: m2[x] = v

print(sum(m1.values()))
print(sum(m2.values()))

