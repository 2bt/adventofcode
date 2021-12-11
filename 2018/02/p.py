import collections
a = b = 0
for l in open("input"):
    d = collections.defaultdict(int)
    for c in l.strip(): d[c] += 1
    v = set(d.values())
    a += 2 in v
    b += 3 in v
print(a * b)

s = set()
for l in open("input"):
    l = l.strip()
    for i in range(len(l)):
        k = l[:i] + "_" + l[i + 1:]
        if k in s:
            print(l[:i] + l[i + 1:])
            exit()
        s.add(k)
