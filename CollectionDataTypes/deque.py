#deque pronounced as 'deck' is an optimised list to perform insertion and deletion easily.

from collections import deque
a=['p','y','t','h','o','n']
d = deque(a)
print(d)

d.append('easy to learn')
print(d)

d.appendleft('Programming language')
print(d)

d.pop()
print(d)

d.popleft()
print(d)