s1 = s2 = 0
for l in open("input"):
    a, b, c = l.split()
    mi, ma = map(int, a.split("-"))
    s1 += mi <= c.count(b[0]) <= ma
    s2 += (c[mi - 1] == b[0]) ^ (c[ma - 1] == b[0])
print(s1, s2)
