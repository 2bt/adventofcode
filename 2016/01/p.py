d = 0
x = 0
y = 0
for a in file("in").read().split(", "):
	d = d + (-1) ** (a[0] == "R") & 3
	x += [0, 1, 0, -1][d] * int(a[1:])
	y += [1, 0, -1, 0][d] * int(a[1:])
print abs(x) + abs(y)




d = 0
x = 0
y = 0
s = set()
def move(n):
	global s, x, y
	for _ in range(n):
		x += [0, 1, 0, -1][d]
		y += [1, 0, -1, 0][d]
		if (x, y) in s:
			print abs(x) + abs(y)
			exit()
		s.add((x, y))


for a in file("in").read().split(", "):
	d = d + (-1) ** (a[0] == "R") & 3
	move(int(a[1:]))

print abs(x) + abs(y)
