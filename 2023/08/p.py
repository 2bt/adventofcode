f = open("input")
a = next(f).strip()
next(f)
g = {l[:3]:[l[7:10], l[12:15]] for l in f}
i = 0
p = "AAA"
while p != "ZZZ":
    d = a[i % len(a)]
    p = g[p][d == "R"]
    i += 1
print(i)

s = len(a)
for p in g:
    if p[2] != "A": continue
    i = 0
    while p[2] != "Z":
        p = g[p][a[i % len(a)] == "R"]
        i += 1
    s *= i // len(a)
print(s)
