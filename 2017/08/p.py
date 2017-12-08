import collections
d = collections.defaultdict(lambda:0)
m = 0
for l in open("input"):
	w = l.split()
	if eval(w[4] + w[5] + w[6], {}, d):
		d[w[0]] = eval(w[0] + "-+"[w[1] == "inc"] + w[2], {}, d)
		m = max(m, d[w[0]])
print max(d.values())
print m
