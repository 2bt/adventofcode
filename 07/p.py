

d = {}
for l in file("in"):
	x, y = l.strip().split(" -> ")
	d[y] = x.split()



# d["b"] = ["956"]

cache = {}
def solve(w):
	if w.isdigit(): return int(w)
	if w in cache: return cache[w]
	a = d[w]
	if len(a) == 1: 		ret = solve(a[0])
	elif a[0] == "NOT": 	ret = ~solve(a[1]) & 0xffff
	elif a[1] == "AND": 	ret = solve(a[0]) & solve(a[2])
	elif a[1] == "OR":		ret = solve(a[0]) | solve(a[2])
	elif a[1] == "RSHIFT":	ret = solve(a[0]) >> int(a[2])
	elif a[1] == "LSHIFT":	ret = solve(a[0]) << int(a[2]) & 0xffff
	else: print "ERROR"
	cache[w] = ret
	return ret


print solve("a")
