s = 0
for l in open("in"):
	w = l.split("-")
	q = w.pop()
	a = "".join(w)
	i = int(q[:3])
	if q[4:-2] == "".join(zip(*sorted(((-a.count(c), c) for c in set(a))))[1])[:5]:
		s += i
		a = " ".join(w)
		for _ in range(i % 26):
			a = "".join([c, chr(97 + (ord(c) - 96) % 26)][c.isalpha()] for c in a)
		if "northpole" in a: print i
print s
