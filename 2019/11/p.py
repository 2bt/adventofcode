PARAM_COUNT = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    9: 1,
    99: 0,
}

class VM:
    def __init__(self, mem, in_cb, out_cb):
        self.mem = mem
        self.input = in_cb
        self.output = out_cb
        self.pc = 0
        self.bp = 0

    def get_mem(self, x):
        if x >= len(self.mem): self.mem.extend([0] * (x + 1 - len(self.mem)))
        return self.mem[x]

    def set_mem(self, x, v):
        if x >= len(self.mem): self.mem.extend([0] * (x + 1 - len(self.mem)))
        self.mem[x] = v

    def run(self):
        while 1:
            op = self.get_mem(self.pc) % 100
            mode = self.get_mem(self.pc) / 100
            self.pc += 1
            p = []
            for _ in range(PARAM_COUNT[op]):
                if   mode % 10 == 0: p.append(self.get_mem(self.pc))
                elif mode % 10 == 1: p.append(self.pc)
                elif mode % 10 == 2: p.append(self.get_mem(self.pc) + self.bp)
                self.pc += 1
                mode /= 10
            if   op == 1: self.set_mem(p[2], self.get_mem(p[0]) + self.get_mem(p[1]))
            elif op == 2: self.set_mem(p[2], self.get_mem(p[0]) * self.get_mem(p[1]))
            elif op == 3: self.set_mem(p[0], self.input())
            elif op == 4: self.output(self.get_mem(p[0]))
            elif op == 5 and self.get_mem(p[0]) != 0: self.pc = self.get_mem(p[1])
            elif op == 6 and self.get_mem(p[0]) == 0: self.pc = self.get_mem(p[1])
            elif op == 7: self.set_mem(p[2], +(self.get_mem(p[0]) < self.get_mem(p[1])))
            elif op == 8: self.set_mem(p[2], +(self.get_mem(p[0]) == self.get_mem(p[1])))
            elif op == 9: self.bp += self.get_mem(p[0])
            elif op == 99: break

mem = map(int, open("input").read().split(","))

s = d = x = y = 0
grid = {}

def in_cb(): return grid.get((x, y), 0)

def out_cb(v):
    global x, y, d, s
    if not s: grid[(x, y)] = v
    else:
        d = (d + [1, -1][v]) % 4
        x += [0, -1, 0, 1][d]
        y += [-1, 0, 1, 0][d]
    s = not s

vm = VM(mem, in_cb, out_cb)
vm.run()
print len(grid)

s = d = x = y = 0
grid = { (0, 0): 1 }
vm = VM(mem, in_cb, out_cb)
vm.run()
ys = sorted(y for x, y in grid)
xs = sorted(x for x, y in grid)
for v in range(ys[0], ys[-1] + 1):
    print "".join(" #"[grid.get((u, v), 0)] for u in range(xs[0], xs[-1] + 1))
