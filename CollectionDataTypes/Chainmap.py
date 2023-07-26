#Chainmap is a dictionary like class for creating a single view of multiple mappings.

from collections import ChainMap
a = {1:'Python',2:'Java'}
b = {3:'Data Science',4:'AIML'}
al = ChainMap(a,b)
print(al)