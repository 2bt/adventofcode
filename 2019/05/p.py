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
            p.append(pc if mode % 10 else mem[pc])
            pc += 1
            mode /= 10
        if   op == 1: mem[p[2]] = mem[p[0]] + mem[p[1]]
        elif op == 2: mem[p[2]] = mem[p[0]] * mem[p[1]]
        elif op == 3: mem[p[0]] = input
        elif op == 4: output = mem[p[0]]
        elif op == 5 and mem[p[0]] != 0: pc = mem[p[1]]
        elif op == 6 and mem[p[0]] == 0: pc = mem[p[1]]
        elif op == 7: mem[p[2]] = mem[p[0]] < mem[p[1]]
        elif op == 8: mem[p[2]] = mem[p[0]] == mem[p[1]]
        elif op == 99: return output

q = list(eval(open("input").read()))
print f(q * 1, 1)
print f(q * 1, 5)
