# we can advantage of the ability to sort a list of tuples to get a sorted version of a dictionary

d = {'a': 10, 'b': 1, "c": 22}

t = d.items()

print t

t.sort()

print t

k = sorted(d.items())

print k

for p, r in sorted(d.items()):
    print p, r

print

tmp = list()
for p, r in d.items():
    tmp.append((r, p))

print tmp

tmp.sort(reverse=True)

print tmp

print

print sorted([(v, k) for k, v in d.items()])

days = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
