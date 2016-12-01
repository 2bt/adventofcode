
t = 2503
for l in file("in"):
	l = l.split()
	s, t1, t2 = [int(l[i]) for i in [3, 6, -2]]

	ts = t1 + t2
	print t / ts * s * t1 + min(t % ts, t1) * s

print


ss = []
for l in file("in"):
	l = l.split()
	ss.append([int(l[i]) for i in [3, 6, -2]] + [0])


for t in range(2503):
	t += 1

	ws = []

	for s in ss:

		ts = s[1] + s[2]
		w = t / ts * s[1] * s[0] + min(t % ts, s[1]) * s[0]
		ws.append(w)

	w_max = max(ws)

	for w, s in zip(ws, ss):
		if w == w_max: s[3] += 1

print max(s[-1] for s in ss)
