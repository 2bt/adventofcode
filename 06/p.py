
f = [[0]*1000 for x in range(1000)]

for l in file("in"):

	l = l.split()
	cmd = l.pop(0)
	if cmd == "turn": cmd = l.pop(0)

	x1, y1 = map(int, l[0].split(","))
	x2, y2 = map(int, l[2].split(","))


	for x in range(x1, x2 + 1):
		for y in range(y1, y2 + 1):

			if cmd == "on": f[x][y] += 1
			elif cmd == "off": f[x][y] = max(0, f[x][y] - 1)
			else: f[x][y] += 2



print sum(map(sum,f))
