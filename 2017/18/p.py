import collections

cmds = [l.split() for l in open("input")]
regs = collections.defaultdict(lambda:0)
val = lambda x: regs[x] if x in regs else int(x)
p = 0
while p < len(cmds):
	cmd = cmds[p]
	p += 1
	o = cmd[0]
	if o == "snd": f = val(cmd[1])
	elif o == "set": regs[cmd[1]] = val(cmd[2])
	elif o == "add": regs[cmd[1]] += val(cmd[2])
	elif o == "mul": regs[cmd[1]] *= val(cmd[2])
	elif o == "mod": regs[cmd[1]] %= val(cmd[2])
	elif o == "rcv":
		if val(cmd[1]) != 0: break
	elif o == "jgz":
		if val(cmd[1]) > 0: p += val(cmd[2]) - 1
print f

class CPU:
	def __init__(self, nr):
		self.nr        = nr
		self.pos       = 0
		self.snd       = 0
		self.queue     = []
		self.regs      = collections.defaultdict(lambda:0)
		self.regs["p"] = nr
	val = lambda self, x: self.regs[x] if x in self.regs else int(x)
	def run(self):
		i = 0
		while self.pos < len(cmds):
			i += 1
			cmd = cmds[self.pos]
			o = cmd[0]
			if o == "snd":
				cpus[not self.nr].queue.append(self.val(cmd[1]))
				self.snd += 1
			elif o == "set": self.regs[cmd[1]] = self.val(cmd[2])
			elif o == "add": self.regs[cmd[1]] += self.val(cmd[2])
			elif o == "mul": self.regs[cmd[1]] *= self.val(cmd[2])
			elif o == "mod": self.regs[cmd[1]] %= self.val(cmd[2])
			elif o == "rcv":
				if not self.queue: return i - 1
				self.regs[cmd[1]] = self.queue.pop(0)
			elif o == "jgz":
				if self.val(cmd[1]) > 0:
					self.pos += self.val(cmd[2])
					continue
			self.pos += 1
		return i

cpus = [CPU(0), CPU(1)]
while cpus[0].run() | cpus[1].run(): pass
print cpus[1].snd
