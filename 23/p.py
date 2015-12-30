i = 0
r = { "a": 1, "b": 0 }
p = [l.split() for l in file("in")]
while i < len(p):
	e = p[i]
	i += 1
	if e[0] == "hlf": r[e[1]] /= 2
	elif e[0] == "tpl": r[e[1]] *= 3
	elif e[0] == "inc": r[e[1]] += 1
	elif e[0] == "jmp": i += int(e[1]) - 1
	elif e[0] == "jie":
		if r[e[1][0]] % 2 == 0: i += int(e[2]) - 1
	elif e[0] == "jio":
		if r[e[1][0]] == 1: i += int(e[2]) - 1
print r
