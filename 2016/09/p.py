a = open("in").read().strip()
s = ""
while a:
	c = a[0]; a = a[1:]
	if c != "(": s += c
	else:
		x, a = a.split(")", 1)
		l, r = map(int, x.split("x"))
		s += a[:l] * r
		a = a[l:]
print len(s)


a = open("in").read().strip()
def f(a):
	i = 0
	while a:
		c = a[0]; a = a[1:]
		if c != "(": i += 1
		else:
			x, a = a.split(")", 1)
			l, r = map(int, x.split("x"))
			if len(a) < l: print "oops"
			i += f(a[:l]) * r
			a = a[l:]
	return i
print f(a)
