a = [(int(l.split()[3]), int(l.strip("\n.").split()[-1]) + i + 1) for i, l in enumerate(open("in"))]
a += [(11, len(a) + 1)]
for i in xrange(10000000):
	if all((y + i) % x == 0 for x, y in a):
		print i
		break
