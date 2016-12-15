#s = ( 0, 0, 1, 2, 2, 2, 2, 0, 1, 0, 0 )
#e = ( 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 )
s = ( 0, 0, 1, 2, 2, 2, 2, 0, 1, 0, 0, 0, 0, 0, 0 )
e = ( 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3 )

def order(a):
	return (a[0],) + sum(sorted((a[i], a[i+1]) for i in range(1, len(a), 2)), ())

q = { order(s) : 0 }
v = set()

def check(a):
	if a in v: return False
	for c in range(2, len(a), 2):
		if a[c] == a[c - 1]: continue
		for g in range(1, len(a), 2):
			if a[c] == a[g]: return False
	return True

while q:
	a = min(q, key=lambda x: q[x] - min(x))
	v.add(a)
	n = q[a]
	del q[a]
	if a == e:
		print n
		break
	for f in a[0] - 1, a[0] + 1:
		if f < 0 or f > 3: continue
		b = list(a)
		b[0] = f
		for i in range(1, len(a)):
			if a[i] != a[0]: continue
			b[i] = f
			t = order(b)
			if check(t): q[t] = n + 1
			for j in range(i + 1, len(a)):
				if b[j] != a[0]: continue
				b[j] = f
				t = order(b)
				if check(t): q[t] = n + 1
				b[j] = a[0]
			b[i] = a[0]
