P, M = map(int, open("input").read().split()[::6])

s = [0] * P
m = [0]
p = [0]
n = [0]
c = 0

for i in range(M * 100):
    if i % 23 < 22:
        o = n[c]
        q = n[o]
        c = len(m)
        n[o] = p[q] = c
        p.append(o)
        n.append(q)
        m.append(i + 1)
    else:
        for _ in range(7): c = p[c]
        s[i % P] += i + 1 + m[c]
        o = p[c]
        c = n[c]
        p[c] = o
        n[o] = c
    if i == M - 1: print(max(s))
print(max(s))
