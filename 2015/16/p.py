a = """children: 3
cats: 7
samoyeds: 2
pomeranians: 3
akitas: 0
vizslas: 0
goldfish: 5
trees: 3
cars: 2
perfumes: 1"""
d = dict(m.split(": ") for m in a.split("\n"))
for l in file("in"):
	s, m = l.strip().split(": ", 1)
	for m in m.split(", "):
		k, v = m.split(": ")
		if k in ["cats", "trees"]:
			if int(d[k]) >= int(v): break
		elif k in ["pomeranians", "goldfish"]:
			if int(d[k]) <= int(v): break
		else:
			if d[k] != v: break
	else: print s
