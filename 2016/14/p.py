import md5, re
def f(m):
	for _ in range(2017): m = md5.new(m).hexdigest()
	return m
h = "ihaygndm"
n = i = 0
c = [f(h + str(x)) for x in range(1000)]
while n < 64:
	c += [f(h + str(i + 1000))]
	t = re.findall("(.)\\1\\1", c.pop(0))
	if t:
		for m in c:
			if t[0] * 5 in m: n += 1; break
	i += 1
print i - 1
