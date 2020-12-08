a = []
for l in open("input"): a.append(int("".join("10"[x in "LF"]for x in l.strip()), 2))

a.sort()
print(a[-1])
for x, y in zip(a, a[1:]):
    if x + 2 == y: print(x + 1)
