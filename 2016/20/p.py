a = sorted(map(int, l.split("-")) for l in open("in"))
i = 0
while i < len(a) - 1:
	x = a[i]
	y = a[i + 1]
	if x[1] + 1 >= y[0]:
		y[0] = x[0]
		y[1] = max(y[1], x[1])
		a.pop(i)
	else: i += 1
print a[0][1] + 1
print sum(y[0] - x[1] - 1 for x, y in zip(a, a[1:]))
