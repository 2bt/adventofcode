a = sorted(map(int,open("input")))

for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] + a[j] == 2020:
            print(a[i] * a[j])
            break

for i in range(len(a) - 2):
    j = i + 1
    k = len(a) - 1
    while j <= k:
        s = a[i] + a[j] + a[k]
        if s == 2020:
            print(a[i] * a[j] * a[k])
            break
        if s > 2020: k -= 1
        if s < 2020: j += 1
