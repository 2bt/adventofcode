a = [map(int, l.split(":")) for l in open("input")]
print sum(x * y for x, y in a if x % (2 * y - 2) == 0)

i = 0
while 1:
	if all((x + i) % (2 * y - 2) for x, y in a): break
	i += 1
print i
