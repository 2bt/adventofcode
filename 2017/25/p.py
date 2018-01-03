import collections

s = "A"
n = 12629077
t = {
	"A": ((1,  1, "B"), (0, -1, "B")),
	"B": ((0,  1, "C"), (1, -1, "B")),
	"C": ((1,  1, "D"), (0, -1, "A")),
	"D": ((1, -1, "E"), (1, -1, "F")),
	"E": ((1, -1, "A"), (0, -1, "D")),
	"F": ((1,  1, "A"), (1, -1, "E")),
}

d = collections.defaultdict(lambda:0)
p = 0
for _ in xrange(n):
	w, m, s = t[s][d[p]]
	d[p] = w
	p += m
print sum(d.itervalues())
