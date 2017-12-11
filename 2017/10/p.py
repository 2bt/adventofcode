def f(lengths, reps=1):
	a = range(256)
	p = 0
	s = 0
	for _ in range(reps):
		for l in lengths:
			for i in range(l / 2):
				j = (p + i) % 256
				k = (p + l - i - 1) % 256
				a[j], a[k] = a[k], a[j]
			p = (p + l + s) % 256
			s += 1
	return a

r = open("input").read().strip()
a = f(map(int, r.split(",")))
print a[0] * a[1]

a = f(map(ord, r) + [17, 31, 73, 47, 23], 64)
print "".join("%02x" % reduce(lambda x, y: x ^ y, a[i:i+16]) for i in range(0, 256, 16))
