a=[[+(c=="#")for c in l.strip()]for l in file("in")]

for _ in range(100):
	a[0][0] = a[-1][0] = a[-1][0] = a[-1][-1] = 1

	b = []
	for y, l in enumerate(a):
		r = []
		for x, c in enumerate(l):
			t = max(0, x-1)
			s = sum(l[t:x+2])
			if y > 0:			s += sum(a[y-1][t:x+2])
			if y < len(l) - 1:	s += sum(a[y+1][t:x+2])
			r.append(+[s==3,3<=s<=4][c])
		b.append(r)
	a = b

#	for l in a: print l
#	print

a[0][0] = a[-1][0] = a[-1][0] = a[-1][-1] = 1

print sum(map(sum,a))
