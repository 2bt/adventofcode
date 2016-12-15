N = 1364
a = [ [ bin(x*x + 3*x + 2*x*y + y + y*y + N).count("1") % 2
	for x in range(50) ] for y in range(50) ]
i = -1
a[1][1] = i
while a[39][31] == 0:
	for y in range(len(a)):
		for x in range(len(a[0])):
			if a[y][x] == 0 and any([
				x < len(a[0]) - 1 and a[y][x+1] == i,
				x > 0 and a[y][x-1] == i,
				y < len(a) - 1 and a[y+1][x] == i,
				y > 0 and a[y-1][x] == i
			]): a[y][x] = i - 1
	i -= 1
print -1 - i


a = [ [ bin(x*x + 3*x + 2*x*y + y + y*y + N).count("1") % 2
	for x in range(50) ] for y in range(50) ]
i = -1
a[1][1] = i
z = 1
for _ in range(50):
	for y in range(len(a)):
		for x in range(len(a[0])):
			if a[y][x] == 0 and any([
				x < len(a[0]) - 1 and a[y][x+1] == i,
				x > 0 and a[y][x-1] == i,
				y < len(a) - 1 and a[y+1][x] == i,
				y > 0 and a[y-1][x] == i
			]): a[y][x] = i - 1; z += 1
	i -= 1
print z
