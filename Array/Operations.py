#length
#Syntax --> len(array_name)
import array as arr
a=arr.array('i',[1,2,3,4,5,6])
print(len(a))

#Adding
#append() add at end of an array
#extend() wants to add more than one element at end of an array
#insert() add an element at a specific position of an array

a.append(5)
print(a)

a.extend([7,8,9,10])
print(a)

a.insert(2,0)
print(a)

#Removing
#pop() remove element and return it
#remove() remove element with a specific value without returning it

print(a.pop())
print(a.pop(9))
print(a)
print(a.pop(-1))

print(a.remove(0))

#Concatenation
print(a)
b = [1,2,3,4,5,6]
c = [7,8,9,10,11,12]
d = b+c
print(d)

#Slicing means fetching some values from an array
# can slice using the : symbol
#This returns a range of elements that we have specified by the index numbers

print(b[0:2])
print(b[0:-3])
print(b[::-1])

#Looping through an array
#We can loop through an array easily using the for and while loops
#for loop iterated over the items of an array specified numbers of times
#While iterated over the elements until a certain condition is met

print(b)
for x in b:
    print(x)

for x in b[0:3]:
    print(x)

temp=0
while temp<d[2]:
    print(d[temp])
    temp=temp+1

temp=0
while temp<len(a):
    print(a[temp])
    temp+=1