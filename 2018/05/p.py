a = open("input").read().strip()

def f(a):
    a = bytearray(a, "ascii")
    i = 0
    while i < len(a) - 1:
        if a[i] == a[i + 1] ^ 32:
            a.pop(i)
            a.pop(i)
            if i > 0: i -= 1
        else: i += 1
    return str(a, "ascii")

a = f(a)
print(len(a))
print(min(len(f(a.replace(x, "").replace(x.upper(), ""))) for x in set(a.lower())))
