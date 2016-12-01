def win(a, d):
	boss = 103
	hp = 100
	while 1:
		boss -= max(1, d - 2)
		if boss <= 0: return True
		hp -= max(1, 9 - a)
		if hp <= 0: return False

rings = [(0, 0,0), (25,1,0), (50,2,0), (100,3,0), (20,0,1), (40,0,2), (80,0,3)]

#z = 999

z = 0

for zd, d in [(8,4), (10,5), (25,6), (40,7), (74,8)]:
	for za, a in [(0,0), (13,1), (31,2), (53,3), (75,4), (102,5)]:
		for zr1, dr1, ar1 in rings:
			for zr2, dr2, ar2 in rings:
				if (zr1, dr1, ar1) == (zr2, dr2, ar2) and zr1 > 0: continue

#				if win(a + ar1 + ar2, d + dr1 + dr2):
#					z = min(z, zd + za + zr1 + zr2)

				if not win(a + ar1 + ar2, d + dr1 + dr2):
					z = max(z, zd + za + zr1 + zr2)

print z
