q = list(eval(open("input").read()))

def f(a):
    p = 0
    while 1:
        c, x, y, z = a[p : p + 4]
        if   c == 1: a[z] = a[x] + a[y]
        elif c == 2: a[z] = a[x] * a[y]
        elif c == 99: break
        else: print "FOO"
        p += 4

a = q * 1
a[1] = 12
a[2] = 2
f(a)
print a[0]

for x in range(100):
    for y in range(100):
        a = q * 1
        a[1] = x
        a[2] = y
        f(a)
        if a[0] == 19690720:
            print x * 100 + y
            break
