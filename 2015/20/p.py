a = 34000000
n = a / 10

m = [0] * n

for i in xrange(1, n):
	for j in xrange(i, n, i): m[j] += i * 10

for i, x in enumerate(m):
	if x >= a:
		print i, x
		break



m = [0] * n

for i in xrange(1, n):
	for j in xrange(i, min(n, i * 51), i): m[j] += i * 11

for i, x in enumerate(m):
	if x >= a:
		print i, x
		break

