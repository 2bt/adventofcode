s = 0
t = 0
for l in open("input"):
	a = map(int, l.split())
	s += max(a) - min(a)
	t += [x / y for x in a for y in a if x != y and x % y == 0][0]
print s
print t
