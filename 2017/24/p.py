import collections

d = collections.defaultdict(lambda:[])
for l in open("input"):
	a, b = sorted(map(int, l.split("/")))
	d[a].append(b)
	d[b].append(a)

def f(null, add):
	def f(v=set(), p=0):
		m = null
		for q in d[p]:
			t = (p, q) if p < q else (q, p)
			if t in v: continue
			v.add(t)
			m = max(m, add(f(v, q), p + q))
			v.remove(t)
		return m
	return f
print f(0, lambda a, b: a + b)()
print f((0, 0), lambda a, b: (a[0] + 1, a[1] + b))()[1]
