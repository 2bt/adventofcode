for d in 1, -1:
	a = map(int, file("input"))
	p = 0
	i = 0
	while p < len(a):
		i += 1
		q = p
		p += a[q]
		a[q] += [d, 1][a[q] < 3]
	print i
