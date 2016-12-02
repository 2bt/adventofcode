x = y = 1
for l in file("in"):
	for c in l:
		x = max(0, min(2, x + (c=="R") - (c=="L")))
		y = max(0, min(2, y + (c=="D") - (c=="U")))
	print x + y * 3 + 1,
print



p = [
	"       ",
	"   1   ",
	"  234  ",
	" 56789 ",
	"  ABC  ",
	"   D   ",
	"       ",
]
x = y = 3
for l in file("in"):
	for c in l:
		x2 = x + (c=="R") - (c=="L")
		y2 = y + (c=="D") - (c=="U")
		if p[y2][x2] != " ": x, y = x2, y2
	print p[y][x],
print
