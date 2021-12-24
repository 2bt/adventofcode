slots = set([2, 4, 6, 8])

def f(s, cache={}):
    r = repr(s)
    if r in cache: return cache[r]
    if s == t: return 0
    e = 9e99
    for i in slots:
        l = i // 2
        x = s[i]
        if x == t[i]: continue

        move_into_slot = True
        k = len(x)
        while k:
            k -= 1
            if x[k] == 0: break
            if x[k] != l:
                move_into_slot = False
                break

        if move_into_slot:
            for rng in range(i - 1, -1, -1), range(i + 1, 11):
                for j in rng:
                    if j in slots: continue
                    if s[j] == l:
                        s[j], x[k] = x[k], s[j]
                        e = min(e, f(s) + (1 + k + abs(i - j)) * 10 ** (l - 1))
                        s[j], x[k] = x[k], s[j]
                    if s[j]: break
            continue

        move_out_of_slot = False
        k = 0
        while k < len(x):
            if x[k] != 0:
                move_out_of_slot = True
                break
            k += 1

        if move_out_of_slot:
            l = x[k]
            for rng in range(i - 1, -1, -1), range(i + 1, 11):
                for j in rng:
                    if j in slots: continue
                    if s[j]: break
                    s[j], x[k] = x[k], s[j]
                    ee = (1 + k + abs(i - j)) * 10 ** (l - 1)
                    e = min(e, f(s) + ee)
                    s[j], x[k] = x[k], s[j]
    cache[r] = e
    return e

for t, s in (
    [0, 0, [1, 1], 0, [2, 2], 0, [3, 3], 0, [4, 4], 0, 0],
    [0, 0, [4, 3], 0, [4, 1], 0, [2, 2], 0, [1, 3], 0, 0],
), (
    [0, 0, [1, 1, 1, 1], 0, [2, 2, 2, 2], 0, [3, 3, 3, 3], 0, [4, 4, 4, 4], 0, 0],
    [0, 0, [4, 4, 4, 3], 0, [4, 3, 2, 1], 0, [2, 2, 1, 2], 0, [1, 1, 3, 3], 0, 0],
):
    print(f(s))
