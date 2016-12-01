import json




def summe(p):
	if type(p) == int: return p
	if type(p) == dict:
		if "red" in p.values(): return 0
		return sum(map(summe, p.values()))
	if type(p) == list: return sum(map(summe, p))
	return 0

p = json.load(file("in"))
print summe(p)
