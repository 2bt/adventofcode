d = {}


for l in file("in"):
	x, _, y, _, s = l.split()
	if x not in d: d[x] = {}
	d[x][y] = int(s)
	if y not in d: d[y] = {}
	d[y][x] = int(s)


def way(l, v, p=None):
	if not v: return l
	return max(way(l + (p and d[p][k] or 0), [c for c in v if c!=k], k) for k in v)


print way(0, d.keys())
