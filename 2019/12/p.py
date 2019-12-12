import itertools
pos = [[int(w[2:]) for w in l[1:-2].split(", ")]for l in open("input")]
vel = [[0, 0, 0] for p in pos]
init_tpos = zip(*pos)
q = {}

for i in xrange(99999999):
    if i == 1000: print sum(sum(map(abs, p)) * sum(map(abs, v)) for p, v in zip(pos, vel))

    if i > 0:
        tpos = zip(*pos)
        tvel = zip(*vel)
        for x in range(3):
            if x in q: continue
            if tpos[x] == init_tpos[x] and tvel[x] == (0, 0, 0, 0):
                q[x] = i
                if len(q) == 3:
                    from fractions import gcd
                    v = 1
                    for x in q.values(): v = v * x / gcd(v, x)
                    print v
                    exit()

    for (p1, v1), (p2, v2) in itertools.combinations(zip(pos, vel), 2):
        for x in range(3):
            s = cmp(p1[x], p2[x])
            v1[x] -= s
            v2[x] += s
    for p, v in zip(pos, vel):
        for x in range(3): p[x] += v[x]


