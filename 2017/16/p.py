cmds = open("input").read().strip().split(",")
a = map(chr, range(ord("a"), ord("a") + 16))
r = ["".join(a)]
while 1:
	for x in cmds:
		if x[0] == "s":
			i = int(x[1:])
			a = a[-i:] + a[:-i]
		else:
			if x[0] == "x": i, j = map(int, x[1:].split("/"))
			else:           i, j = map(a.index, x[1::2])
			a[i], a[j] = a[j], a[i]
	l = "".join(a)
	if l == r[0]: break
	r.append(l)

print r[1]
print r[1000000000 % len(r)]
