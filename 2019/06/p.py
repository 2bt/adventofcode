d = {}
for l in open("input"):
    a, b = l.strip().split(")")
    d[b] = a

c = 0
for k in d:
    while k in d: k = d[k]; c += 1
print c

def f(k):
    p = []
    while k in d: p.append(k); k = d[k]
    return p

a = f("SAN")
b = f("YOU")
while a[-1] == b[-1]: a.pop(); b.pop()
print len(a) + len(b) - 2
