weight = {}
kids = {}
names = set()
for l in open("input"):
	w = l.strip().split(" ", 3)
	name = w.pop(0)
	names.add(name)
	weight[name] = int(w.pop(0)[1:-1])
	kids[name] = w[1].split(", ") if w else []

for ks in kids.itervalues():
	for k in ks:
		if k in names: names.remove(k)

root = names.pop()
print root

def totalWeight(n):
	ks = kids[n]
	ws = map(totalWeight, ks)
	if not ws: return weight[n]
	i = min(range(len(ks)), key=lambda x:ws.count(ws[x]))
	d = ws[i - 1] - ws[i]
	if d == 0: return weight[n] + sum(ws)
	print weight[ks[i]] + d
	exit()
totalWeight(root)
