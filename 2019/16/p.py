A = map(int, open("input").read().strip())
a = A * 1
b = [0] * len(a)
for _ in range(100):
    s = [0]
    for x in a: s.append(s[-1] + x)
    for n in xrange(0, len(a)):
        i = n
        c = 0
        q = 1
        while i < len(a):
            m = min(len(a), i + n + 1)
            c += (s[m] - s[i]) * q
            i += (n + 1) * 2
            q *= -1
        b[n] = abs(c) % 10
    a, b = b, a
print "".join(map(str, a[:8]))


a = A * 10000
b = [0] * len(a)
o = 0
for i, x in enumerate(a[:7]): o = o * 10 + x
assert o > len(a) / 2
for _ in range(100):
    c = 0
    for i in range(len(a) - 1, o - 1, -1):
        b[i] = c = (c + a[i]) % 10
    a, b = b, a

print "".join(map(str, a[o:o + 8]))
