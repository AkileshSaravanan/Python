#OrderedDict is dictionary subclass which remembers the order in which the entries were done

from collections import OrderedDict
d=OrderedDict()
d[1]='p'
d[2]='y'
d[3]='t'
d[4]='h'
d[5]='o'
d[6]='n'
print(d)

print(d.keys())

print(d.items())

d[1]='J'
print(d)