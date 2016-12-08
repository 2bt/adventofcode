import sys, time
a = [[" "] * 50 for _ in range(6)]
for l in open("in"):
	if "rect" in l:
		w, h  = map(int, l[5:].split("x"))
		for x in range(w):
			for y in range(h): a[y][x] = "#"
	if "row" in l:
		y, n = map(int, l[13:].split("by"))
		a[y] = a[y][-n:] + a[y][:-n]
	if "column" in l:
		x, n = map(int, l[16:].split("by"))
		a = map(list, zip(*a))
		a[x] = a[x][-n:] + a[x][:-n]
		a = map(list, zip(*a))

	sys.stdout.write("\x1b[;f")
	for l in a: print "".join(l)
	time.sleep(0.1)

print sum(a, []).count("#")
