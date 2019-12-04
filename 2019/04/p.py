c = d = 0
for x in xrange(168630, 718098 + 1):
    s = str(x)
    if s != "".join(sorted(s)): continue
    c += len(set(s)) < 6
    d += any(s.count(q) == 2 for q in s)
print c, d
