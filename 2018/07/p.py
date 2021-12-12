from collections import defaultdict

d = defaultdict(set)
e = defaultdict(set)
for l in open("input"):
    w = l.split()
    d[w[7]].add(w[1])
    e[w[1]].add(w[7])

q = ""
s = set(e) - set(d)
while s:
    x = min(s)
    q += x
    s.remove(x)
    for y in e[x]:
        d[y].remove(x)
        if not d[y]: s.add(y)
print(q)


d = defaultdict(set)
e = defaultdict(set)
for l in open("input"):
    w = l.split()
    d[w[7]].add(w[1])
    e[w[1]].add(w[7])

workers    = set()
next_steps = set(e) - set(d)
time       = 0
while next_steps or workers:

    # assign steps to workers
    while next_steps and len(workers) < 5:
        x = min(next_steps)
        next_steps.remove(x)
        workers.add((time + 61 + ord(x) - ord("A"), x))

    # move time forward
    time = min(w)[0]

    # remove workers and collect new next steps
    w = set()
    for t, x in workers:
        if time == t:
            for y in e[x]:
                d[y].remove(x)
                if not d[y]: next_steps.add(y)
        else: w.add((t, x))
    workers = w

print(time)
