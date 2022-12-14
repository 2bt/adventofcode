for R, D in (20, 3), (10000, 1):
    items   = []
    ops     = []
    tests   = []
    dsts    = []
    inspect = []
    N = 1
    for m in open("input").read().split("\n\n"):
        _, l1, l2, l3, l4, l5 = m.strip().split("\n")
        items.append([int(x) for x in l1[17:].split(",")])
        ops.append(l2[18:])
        tests.append(int(l3.split()[-1]))
        dsts.append([
            int(l5.split()[-1]),
            int(l4.split()[-1]),
        ])
        inspect.append(0)
        N *= tests[-1]
    for _ in range(R):
        for n in range(len(items)):
            for i in items[n]:
                i = eval(ops[n], {"old": i}) % N // D
                items[dsts[n][i % tests[n] == 0]].append(i)
            inspect[n] += len(items[n])
            items[n] = []
    x, y = sorted(inspect)[-2:]
    print(x * y)
