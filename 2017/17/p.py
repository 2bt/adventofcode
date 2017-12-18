s = 394
f = [0]
p = 0
for i in range(1, 2018):
	p = (p + s) % i + 1
	f.insert(p, i)
print f[p + 1]

for i in xrange(2018, 50000001):
	p = (p + s) % i + 1
	if p == 1: f = i
print f
