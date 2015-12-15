a=file("q").read()

s = {(0, 0)}

x = y = 0
for c in a[::2]:
	if c == ">": x += 1
	if c == "<": x -= 1
	if c == "^": y += 1
	if c == "v": y -= 1
	s.add((x, y))

x = y = 0
for c in a[1::2]:
	if c == ">": x += 1
	if c == "<": x -= 1
	if c == "^": y += 1
	if c == "v": y -= 1
	s.add((x, y))

print len(s)
