n = 3001330
a = range(n)
i = 0
while len(a) > 1: i, a = i ^ len(a) % 2, a[i::2]
print a[0] + 1


#for n in range(1, 101):
#	a = range(n)
#	while len(a) > 1:
#		a.pop(len(a) / 2)
#		a.append(a.pop(0))
#	print "%3d" % n, "#" * (a[0] + 1)


def p2(n):
	c = 1
	for e in range(20):
		for i in range(3 ** e):
			c += 1
			if c == n: return i + 1
		for i in range(3 ** e):
			c += 1
			if c == n: return 3 ** e + (i + 1) * 2
print p2(n)
