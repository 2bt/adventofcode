p = 0, 0, 0
l = 0
d = {
	"n":  ( 0, 1,-1),
	"s":  ( 0,-1, 1),
	"ne": ( 1, 0,-1),
	"sw": (-1, 0, 1),
	"nw": ( 1,-1, 0),
	"se": (-1, 1, 0),
}
for w in open("input").read().strip().split(","):
	p = [a + b for a, b in zip(p, d[w])]
	l = max(map(abs, p) + [l])
print max(map(abs, p))
print l
