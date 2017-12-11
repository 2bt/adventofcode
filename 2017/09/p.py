score = 0
trash = 0
depth = 0
f = open("input")
while 1:
	c = f.read(1)
	if not c: break
	if c == "{":
		depth += 1
		score += depth
		continue
	if c == "}":
		depth -= 1
		continue
	if c == "<":
		while 1:
			c = f.read(1)
			if c == ">": break
			if c == "!": f.read(1)
			else: trash += 1
		continue
print score
print trash
