import itertools

d = {}


for l in file("in"):

	f = l.split()

	a = f[0]
	b = f[-1][:-1]
	i = int(f[3])
	if f[2] == "lose": i *= -1

	d[a] = d.get(a, {})
	d[a][b] = d[a].get(b, 0) + i

	d[b] = d.get(b, {})
	d[b][a] = d[b].get(a, 0) + i





ks = set()
for k, v in d.items():
	ks = ks.union(set([k] + v.keys()))


d["I"] = {}
for k in ks:
	d[k]["I"] = 0
	d["I"][k] = 0

ks.add("I")




a = 0

for l in itertools.permutations(ks):
	m = sum(d[l[i-1]][l[i]] for i in range(len(l)))
	a = max(a, m)

print a

