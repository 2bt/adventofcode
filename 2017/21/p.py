rules = {}
for l in open("input"):
	src, dst = [w.split("/") for w in l.strip().split(" => ")]
	for _ in range(4):
		rules[tuple(src)] = dst
		rules[tuple(src[::-1])] = dst
		src = map("".join, zip(*src[::-1]))

def f(a):
	w = [3, 2][len(a) % 2 == 0]
	b = [""] * (len(a) + len(a) / w)
	for y in range(len(a) / w):
		for x in range(len(a) / w):
			src = tuple(a[y*w+i][x*w:x*w+w] for i in range(w))
			for i, x in enumerate(rules[src]): b[y*(w+1)+i] += x
	return b

a = ".#./..#/###".split("/")

for _ in range(5): a = f(a)
print sum(l.count("#") for l in a)

for _ in range(13): a = f(a)
print sum(l.count("#") for l in a)
