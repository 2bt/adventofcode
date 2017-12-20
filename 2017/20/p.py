q = [[map(int, w[3:-1].split(",")) for w in l.strip().split(", ")] for l in open("input")]
print min(enumerate(q), key=lambda(i,(p,v,a)):sum(map(abs,a)))[0]

import collections
for _ in xrange(100):
	d = collections.defaultdict(lambda:0)
	for l in q:
		l[1] = map(sum,zip(l[1], l[2]))
		l[0] = tuple(map(sum,zip(l[0], l[1])))
		d[l[0]] += 1
	q = filter(lambda l:d[l[0]] == 1, q)
print len(q)
