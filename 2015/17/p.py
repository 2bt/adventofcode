d = {}
def f(a, s=0, c=0):
	if s == 150:
		d[c] = d.get(c, 0) + 1
		return 1
	if a == [] or s > 150: return 0
	return sum(f(a[i+1:], s+a[i], c+1) for i in range(len(a)))
print f(map(int, file("in")))
print d[min(d.keys())]
