import md5
q = [(0, 0, "pxxbnzuo")]
while q:
	x, y, m = q.pop(0)
	if x == y == 3:
		print m[8:], len(m[8:])
		continue
	for i, c in enumerate(md5.new(m).hexdigest()[:4]):
		if c < "b": continue
		if i == 0 and y == 0: continue
		if i == 1 and y == 3: continue
		if i == 2 and x == 0: continue
		if i == 3 and x == 3: continue
		q += [(x + [0, 0, -1, 1][i], y + [-1, 1, 0, 0][i], m + "UDLR"[i])]
	q.sort(key=lambda x:len(x[2]))
