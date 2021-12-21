import collections

ss = [set()]
for l in open("input"):
    if not l.strip(): ss.append(set())
    if not "," in l: continue
    ss[-1].add(tuple(map(int, l.split(","))))

turn = lambda x, y, z: (-y, x, z)
roll = lambda x, y, z: (x, -z, y)
R = [
    turn, turn, turn, roll,
    turn, turn, turn, roll,
    turn, turn, turn, lambda x, y, z: (y, z, x)
] * 2

def sub(a, b):
    x, y, z = a
    u, v, w = b
    return x - u, y - v, z - w

ps = ss.pop(0)
aa = [ps]
positions = [(0, 0, 0)]

while aa:
    s1 = aa.pop()
    j = 0
    while j < len(ss):
        s2 = ss[j]
        for r in R:
            s2 = set(r(*x) for x in s2)
            d = collections.defaultdict(int)
            for a in s1:
                for b in s2: d[sub(b, a)] += 1
            m = max(d, key=d.__getitem__)
            if d[m] >= 12: break
        else:
            j += 1
            continue
        positions.append(m)
        s2 = set(sub(x, m) for x in s2)
        aa.append(s2)
        ps |= s2
        ss.pop(j)

print(len(ps))
print(max(sum(map(abs, sub(a, b))) for a in positions for b in positions))
