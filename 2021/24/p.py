from functools import cache

cmds = open("input").readlines()
var1, var2, var3 = [[int(x.split()[2]) for x in cmds[i::len(cmds) // 14]] for i in [4, 5, 15]]

for q in -1, 1:
    @cache
    def f(i, s):
        if s > 26 ** 5: return False, ""
        if i == len(var1): return s == 0, ""
        for input in range(1, 10)[::q]:
            z = s
            x = input != z % 26 + var2[i]
            z = z // var1[i] * (25 * x + 1)
            z += x * (input + var3[i])
            b, d = f(i + 1, z)
            if b: return True, str(input) + d
        return False, []
    print(f(0, 0)[1])
