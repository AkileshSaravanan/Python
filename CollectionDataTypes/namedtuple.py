#namedtuple() returns a tuple with a named value for each element in the tuple
#it overcomes the problem of accessing the elements

from collections import namedtuple
a = namedtuple('courses','name,technology')
s = a('data science','python')
print(s)

a = namedtuple('courses','name,technology')
s = a._make(['artificial intelligence','python'])
print(s)