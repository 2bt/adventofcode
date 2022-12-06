for Q in -1, 1:
    f = open("input")
    q = f.read(36 * 9 + 1)
    stacks = [list(q[1 + i * 4::36][-2::-1].strip()) for i in range(9)]
    for l in f:
        n, x, y = map(int, l.split()[1::2])
        stacks[y - 1] += stacks[x - 1][-n:][::Q]
        del stacks[x - 1][-n:]
    print("".join(s[-1] for s in stacks))
