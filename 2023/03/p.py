import string, collections
g = open("input").read()
L = g.find("\n") + 1
g += " " * L
s1 = s2 = 0
gear_c = collections.defaultdict(int)
gear_p = collections.defaultdict(lambda:1)
p = 0
while p < len(g):
    if not g[p].isdigit():
        p += 1
        continue
    q = p
    while g[p].isdigit(): p += 1
    o = list(range(q - 1 - L, p + 1 - L)) + [q - 1, p] + list(range(q - 1 + L, p + 1 + L))
    if set(g[x] for x in o) - set(string.digits + ".\n "): s1 += int(g[q:p])
    for x in o:
        if g[x] == "*":
            gear_c[x] += 1
            gear_p[x] *= int(g[q:p])
for x in gear_c:
    if gear_c[x] == 2: s2 += gear_p[x]
print(s1, s2)
