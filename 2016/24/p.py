m = {}
for c in range(10):
	a = map(list, open("in"))
	for l in a:
		i = "".join(l).find(str(c))
		if i != -1:
			l[i] = 0
			break
	else: break
	m[c] = {}
	for i in xrange(500):
		done = True
		for y in xrange(1, len(a) - 1):
			for x in xrange(1, len(a[0]) - 1):
				d = a[y][x]
				if d == "#" or type(d) != str: continue
				if i in (
				a[y - 1][x],
				a[y + 1][x],
				a[y][x - 1],
				a[y][x + 1]):
					done = False
					a[y][x] = i + 1
					if d in "01234567": m[c][int(d)] = i + 1
		if done: break

def f(p, q, z):
	if not q: return [0, m[p][0]][z]
	return min(m[p][q[i]] + f(q[i], q[:i] + q[i+1:], z) for i in range(len(q)))


print f(0, m.keys()[1:], False)
print f(0, m.keys()[1:], True)
