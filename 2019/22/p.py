# f(x) = ax + b mod N
# g(x) = cx + d mod N
# g(f(x)) = c(ax + b) + d mod N
# g(f(x)) = cax + cb + d mod N
a, b = 1, 0
for l in open("input"):
    if l.startswith("deal into"):   c, d = -1, -1
    elif l.startswith("deal with"): c, d = int(l.split()[-1]), 0
    else:                           c, d = 1, -int(l.split()[-1])
    a, b = c * a, c * b + d
print((a * 2019 + b) % 10007)
N = 119315717514047
C = 101741582076661
a, b, c, d = 1, 0, a, b
while C:
    if C & 1: a, b = c * a % N, (c * b + d) % N
    C //= 2
    c, d = c * c % N, (c * d + d) % N
def inverse(a, N):
    # a**-1 = a**(N-2) % N
    n = N - 2
    x = 1
    while n:
        if n & 1: x = (x * a) % N
        a = (a * a) % N
        n //= 2
    return x
print((2020 - b) * inverse(a, N) % N)
