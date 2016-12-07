print "".join(max(l, key=l.count) for l in zip(*file("in")))
print "".join(min(l, key=l.count) for l in zip(*file("in")))
