#Counter is a dictionary subclass for counting hashable objects

from collections import Counter

a=[1,1,1,1,2,2,2,3,1,3,3,4,4,5,5,6,6]
c = Counter(a)
print(c)

print(list(c.elements()))

print(c.most_common())

sub={2:1,6:1}
print(c.subtract(sub))
print(c.most_common())
