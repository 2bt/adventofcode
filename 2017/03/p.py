a = 347991

b = 1
l = 8
while 1:
	if b + l >= a: break
	b += l
	l += 8
q = l / 4
print [max(q - i, i) for i in range(1, q + 1)][(a - b - 1) % q]

import collections
f = collections.defaultdict(lambda: 0)
d = 0
x = 0
y = 0
f[x, y] = 1
while f[x, y] <= a:
	x += [0, 1, 0, -1][d]
	y += [1, 0, -1, 0][d]
	f[x, y] = sum(f[s, t] for s in range(x - 1, x + 2) for t in range(y - 1, y + 2))
	d2 = (d + 1) % 4
	s = x + [0, 1, 0, -1][d2]
	t = y + [1, 0, -1, 0][d2]
	if f[s, t] == 0: d = d2
print f[x, y]
