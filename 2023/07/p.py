def t(v):
    if   v == [5]:         return 7
    elif v == [1, 4]:      return 6
    elif v == [2, 3]:      return 5
    elif v[-1] == 3:       return 4
    elif v[-2:] == [2, 2]: return 3
    elif v[-1] == 2:       return 2
    else:                  return 1
ks = []
qs = []
for l in open("input"):
    h, b = l.split()
    v = sorted(map(h.count, set(h)))
    ks.append([t(v)] + ["23456789TJQKA".find(x) for x in h] + [int(b)])
    v = sorted(map(h.count, set(h) - set("J"))) or [0]
    v[-1] += h.count("J")
    qs.append([t(v)] + ["J23456789TQKA".find(x) for x in h] + [int(b)])
print(sum((i + 1) * x.pop() for i, x in enumerate(sorted(ks))))
print(sum((i + 1) * x.pop() for i, x in enumerate(sorted(qs))))
