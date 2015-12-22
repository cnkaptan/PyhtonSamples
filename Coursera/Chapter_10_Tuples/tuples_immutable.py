# listenin aksine tupleler immutable dir. icerigi degistirilemez

x = [9, 8, 7]
x[2] = 6
print x

"""
y = "ABC"
y[2] = 'D'
"""

z = (5, 4, 3)
# z[2] = 0

lst = list()
tpl = tuple()

print dir(lst)
print dir(tpl)
