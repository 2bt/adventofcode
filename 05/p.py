
s = 0

for l in file("in"):

#	if sum(l.count(v) for v in "aeiou") < 3: continue
#	if not any(a==b for a,b in zip(l, l[1:])): continue
#	if any(x in l for x in ("ab", "cd", "pq", "xy")): continue


	if not any(l.count(l[i:i+2]) > 1 for i in range(len(l) - 1)): continue

	if not any(l[i] == l[i + 2] for i in range(len(l) - 2)): continue


	s += 1



print s
