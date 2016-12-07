s = 0
for l in open("in"):
	f = 0; q = [0, 0]
	for i in range(len(l) - 4):
		a,b,c,d = l[i:i+4]
		f ^= a in "[]"
		q[f] |= a == d != b == c
	s += q[0] and not q[1]
print s

s = 0
for l in open("in"):
	f = 0
	s1 = set()
	s2 = set()
	for i in range(len(l) - 3):
		a,b,c = l[i:i+3]
		f ^= a in "[]"
		if a == c != b:
			if f: s1.add(a + b)
			else: s2.add(b + a)
	if s1 & s2: s += 1
print s

