#defaultdict is a dictionary subclass which calls a factory function to supply missing values

from collections import defaultdict

d= defaultdict(int)
d[1]='python'
d[2]='Java'
print(d)
print(d[3])

#error because 3 is not present inside this ordinary dictionary
a={1:'python',2:'java'}
print(a[3])