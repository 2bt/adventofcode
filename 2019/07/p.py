PARAM_COUNT = {
    1: 3,
    2: 3,
    3: 1,
    4: 1,
    5: 2,
    6: 2,
    7: 3,
    8: 3,
    99: 0,
}

class VM:
    def __init__(self, mem, input):
        self.mem = mem
        self.input = input
        self.pc = 0

    def run(self):
        while 1:
            op = self.mem[self.pc] % 100
            mode = self.mem[self.pc] / 100
            self.pc += 1
            p = []
            for _ in range(PARAM_COUNT[op]):
                p.append(self.pc if mode % 10 else self.mem[self.pc])
                self.pc += 1
                mode /= 10
            if   op == 1: self.mem[p[2]] = self.mem[p[0]] + self.mem[p[1]]
            elif op == 2: self.mem[p[2]] = self.mem[p[0]] * self.mem[p[1]]
            elif op == 3: self.mem[p[0]] = self.input.pop(0)
            elif op == 4: return self.mem[p[0]]
            elif op == 5 and self.mem[p[0]] != 0: self.pc = self.mem[p[1]]
            elif op == 6 and self.mem[p[0]] == 0: self.pc = self.mem[p[1]]
            elif op == 7: self.mem[p[2]] = self.mem[p[0]] < self.mem[p[1]]
            elif op == 8: self.mem[p[2]] = self.mem[p[0]] == self.mem[p[1]]
            elif op == 99: return None

mem = map(int, open("input").read().split(","))

import itertools

def f(settings):
    mv = 0
    for ss in itertools.permutations(settings):
        vms = [VM(mem * 1, [s]) for s in ss]
        v = 0
        for vm in itertools.cycle(vms):
            vm.input.append(v)
            o = vm.run()
            if o == None: break
            v = o
        mv = max(v, mv)
    return mv

print f(range(5))
print f(range(5, 10))
