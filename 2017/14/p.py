def knot(word):
	lengths = map(ord, word) + [17, 31, 73, 47, 23]
	a = range(256)
	p = 0
	s = 0
	for _ in range(64):
		for l in lengths:
			for i in range(l / 2):
				j = (p + i) % 256
				k = (p + l - i - 1) % 256
				a[j], a[k] = a[k], a[j]
			p = (p + l + s) % 256
			s += 1
	return "".join("%02x" % reduce(lambda x, y: x ^ y, a[i:i+16]) for i in range(0, 256, 16))

a = "wenycdww"

table = { hex(i)[2:] : "".join(".#"[i & (8>>j) > 0] for j in range(4)) for i in range(16) }

grid = []
used = 0
for i in range(128):
	l = "".join(table[c] for c in knot(a + "-%d" % i))
	used += l.count("#")
	grid.append(list(l))

def f(x, y):
	if x < 0 or y < 0 or x > 127 or y > 127: return 0
	if grid[y][x] == ".": return 0
	grid[y][x] = "."
	f(x - 1, y)
	f(x + 1, y)
	f(x, y - 1)
	f(x, y + 1)
	return 1

regs = 0
for x in range(128):
	for y in range(128): regs += f(x, y)

print used
print regs
