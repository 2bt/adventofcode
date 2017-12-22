import collections

def init():
	global grid, pos, dir, count
	grid = collections.defaultdict(lambda:0)
	for y, l in enumerate(open("input")):
		for x, count in enumerate(l):
			if count == "#": grid[x, y] = 2
	pos = 12, 12
	dir = 0, -1
	count = 0

init()
for _ in xrange(10000):
	if grid[pos]:
		grid[pos] = 0
		dir = -dir[1], dir[0]
	else:
		grid[pos] = 2
		dir = dir[1], -dir[0]
		count += 1
	pos = pos[0] + dir[0], pos[1] + dir[1]
print count

init()
for _ in xrange(10000000):
	x = grid[pos]
	if x == 0:
		grid[pos] = 1
		dir = dir[1], -dir[0]
	elif x == 1:
		grid[pos] = 2
		count += 1
	elif x == 2:
		grid[pos] = 3
		dir = -dir[1], dir[0]
	elif x == 3:
		grid[pos] = 0
		dir = -dir[0], -dir[1]
	pos = pos[0] + dir[0], pos[1] + dir[1]
print count
