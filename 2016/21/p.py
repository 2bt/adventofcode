s = "abcdefgh"
for l in open("in"):
	w = l.split()
	if w[0] == "rotate":
		if w[1] in ("right", "left"):
			i = (-1)**(w[1] == "right") * int(w[2])
			s = s[i:] + s[:i]
		else:
			i = s.find(w[6])
			i += 1 + (i > 3)
			for _ in range(i): s = s[-1:] + s[:-1]
	elif w[0] == "swap":
		if w[1] == "letter":
			t = w[2] + w[5]
			s = "".join((t + c + c)[t.find(c) ^ 1] for c in s)
		else:
			s = list(s)
			s[int(w[2])], s[int(w[5])] = s[int(w[5])], s[int(w[2])]
			s = "".join(s)
	elif w[0] == "move":
		c = s[int(w[2])]
		s = s[:int(w[2])] + s[int(w[2]) + 1:]
		s = s[:int(w[5])] + c + s[int(w[5]):]
	else: # reverse
		s = s[:int(w[2])] + s[int(w[2]):int(w[4]) + 1][::-1] + s[int(w[4]) + 1:]
print s



s = "fbgdceah"
for l in list(open("in"))[::-1]:
	w = l.split()
	if w[0] == "rotate":
		if w[1] in ("right", "left"):
			i = (-1)**(w[1] == "left") * int(w[2])
			s = s[i:] + s[:i]
		else:
			for j in range(99):
				s = s[1:] + s[:1]
				i = s.find(w[6])
				i += (i > 3)
				if i == j: break
	elif w[0] == "swap":
		if w[1] == "letter":
			t = w[2] + w[5]
			s = "".join((t + c + c)[t.find(c) ^ 1] for c in s)
		else:
			s = list(s)
			s[int(w[2])], s[int(w[5])] = s[int(w[5])], s[int(w[2])]
			s = "".join(s)
	elif w[0] == "move":
		c = s[int(w[5])]
		s = s[:int(w[5])] + s[int(w[5]) + 1:]
		s = s[:int(w[2])] + c + s[int(w[2]):]
	else: # reverse
		s = s[:int(w[2])] + s[int(w[2]):int(w[4]) + 1][::-1] + s[int(w[4]) + 1:]
print s


