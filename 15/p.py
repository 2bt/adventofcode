

m = [[int(n.split()[1]) for n in l.strip().split(": ")[1].split(", ")] for l in file("in")]
print m




def calc(q):
	f = 1
	for i in range(4): f *= max(0, sum(w*z[i] for w, z in zip(q, m)))
	return f, max(0, sum(w*z[4] for w, z in zip(q, m)))



s = 0

for a in range(101):
	for b in range(101 - a):
		for c in range(101 - a - b):
			d = 100 - a - b - c


			w, cals = calc([a, b, c, d])
			if s < w and cals == 500:
				s = w
				print a, b, c, d, w

print s
