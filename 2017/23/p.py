import collections

cmds = [l.split() for l in open("input")]

class CPU:
	def __init__(self):
		self.pos  = 0
		self.muls = 0
		self.regs = collections.defaultdict(lambda:0)
	val = lambda self, x: self.regs[x] if x.isalpha() else int(x)
	def run(self):
		i = 0
		while self.pos < len(cmds):
			i += 1
			cmd = cmds[self.pos]
			o = cmd[0]
			if o == "set": self.regs[cmd[1]] = self.val(cmd[2])
			elif o == "sub": self.regs[cmd[1]] -= self.val(cmd[2])
			elif o == "mul":
				self.regs[cmd[1]] *= self.val(cmd[2])
				self.muls += 1
			elif o == "jnz":
				if self.val(cmd[1]):
					self.pos += self.val(cmd[2])
					continue
			self.pos += 1
		return i

c = CPU()
c.run()
print c.muls


def is_prime(x):
	if x % 2 == 0: return False
	for i in xrange(3, int(x**0.5 + 1), 2):
		if x % i == 0: return False
	else: return True
b = 106500
h = 0
while 1:
	h += not is_prime(b)
	if b == 123500 : break
	b += 17

print h
