nodes = []
for l in list(open("in"))[2:]:
	w = l.split()
	nodes += [( w[0], int(w[1][:-1]), int(w[2][:-1]), int(w[3][:-1]) )]



p = set()
q = set()
for i in range(len(nodes)):
	n = nodes[i]
	for j in range(i + 1, len(nodes)):
		m = nodes[j]
		if n[2] <= m[3] and m[2] <= n[3]:
			p.add((n, m))
			q.add(n)
			q.add(m)
print len(p)

i = 0
for x in range(33):
	for y in range(30):
		n = nodes[i]
		c = "#"
		if n[0] == "/dev/grid/node-x32-y0": c = "G"
		elif n[2] == 0: c = "_"
		elif n in q: c = "."
		print c,
		i += 1
	print

print 70 + 31 * 5
