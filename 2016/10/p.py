from collections import defaultdict
b = defaultdict(lambda:[])
v = defaultdict(lambda:[])

for l in open("in"):
	w = l.split()
	if w[0] == "bot": b[w[0] + w[1]] = w[5] + w[6], w[10] + w[11]
	else: v[w[4] + w[5]] += [int(w[1])]

q = [x for x in b.keys() if len(v[x]) > 1]
while q:
	x = q.pop()
	v[x].sort()
	if v[x] == [17, 61]: print x.strip("bot")
	v[b[x][1]] += [v[x].pop()]
	v[b[x][0]] += [v[x].pop()]
	if len(v[b[x][0]]) == 2: q += [b[x][0]]
	if len(v[b[x][1]]) == 2: q += [b[x][1]]

print v["output0"][0] * v["output1"][0] * v["output2"][0]
