for m in max, min: print "".join(m(l, key=l.count) for l in zip(*file("in")))
