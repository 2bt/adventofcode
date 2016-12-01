a = bytearray("vzbxkghb")


for _ in range(2):
	while 1:
		for i in range(7, 0, -1):
			a[i] += 1
			if a[i] <= 122: break
			a[i] = 'a'
		if not any(a[i]==a[i+1]-1==a[i+2]-2 for i in range(6)): continue
		if any(c in a for c in "iol"): continue
		if len(set(a[i] for i in range(7) if a[i] == a[i+1])) < 2: continue
		break
	print a
