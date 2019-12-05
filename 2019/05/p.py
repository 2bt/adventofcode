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

def f(mem, input):
    pc = 0
    while 1:
        op = mem[pc] % 100
        mode = mem[pc] / 100
        pc += 1
        p = []
        for _ in range(PARAM_COUNT[op]):
            x = pc
            pc += 1
            if mode % 10 == 0: x = mem[x]
            mode /= 10
            p.append(x)
        if   op == 1: mem[p[2]] = mem[p[0]] + mem[p[1]]
        elif op == 2: mem[p[2]] = mem[p[0]] * mem[p[1]]
        elif op == 3: mem[p[0]] = input
        elif op == 4: output = mem[p[0]]
        elif op == 5:
            if mem[p[0]] != 0: pc = mem[p[1]]
        elif op == 6:
            if mem[p[0]] == 0: pc = mem[p[1]]
        elif op == 7: mem[p[2]] = mem[p[0]] < mem[p[1]]
        elif op == 8: mem[p[2]] = mem[p[0]] == mem[p[1]]
        elif op == 99: return output

q = list(eval(open("input").read()))
print f(q * 1, 1)
print f(q * 1, 5)
