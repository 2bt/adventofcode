c = 20151125

i = 0
while 1:
	i += 1
	for m in range(0, i):
		y = i - m
		x = m + 1
		if y == 2981 and x == 3075:
			print c
			print q
		c = c * 252533 % 33554393
