import re
p = 0
q = 0
for l in open("input"):
    a, b, c, d = map(int, re.findall(r"\d+", l))
    p += a <= c and b >= d or c <= a and d >= b
    q += not (a > d or b < c)
print(p)
print(q)
