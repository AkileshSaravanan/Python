#Variable is a memory location where u can store a value
#Variables in python are case-sensitive

a = 10
print(10)

A = 20
print(A)

#Datatypes are mainly 6 types
#Numbers String List Dictionary Tuple Set Range
#Range is mainly used for iterating two value or using for loops

#Numbers are Integer Float Complex Boolean
x=10
print(type(x))

x=10.2
print(type(x))

x=10j
print(type(x))

num = 10>9
print(type(num))

#String are Single or Double quotes
#String are immutable
x = 'Ram'
print(len(x))

print(x[0:3])
print(x[1:3])
print(x[0:6])
print(x[-2])

print(x.upper())

print(x.lower())

#List is a collection of array which is changeable in order which they have indexes just like string
#We use square brackets to declare a list
#Duplicate elements are possible
#Different datatype can possible

list1 = ["apple","banana",10,20,10,30]
print(list1)

#We can update list by index
list1[4] = 40
print(list1)
#append the list
list1.append(50)
print(list1)
#insert value at middle using insert()
list1.insert(5,60)
print(list1)

#Reverse
list1.reverse()
print(list1)

#Dictionaries are collection like list,but it is unordered, changeable and indexed
#We have a key value pair in a dictionary
#No duplicates entries are present
course = {1:"python",2:"Data science","third":"Java"}
print(course)

print(course["third"])

print(course.get("third"))

course["third"] = "C"
print(course)

course["four"]="machine learning"
print(course)

#Tuple is ordered and cannot be changed
#It is immutable but duplicate values can be present
animals = (10,10,20,'tiger','lion','peacock','lion')
print(animals)

print(animals[2])

print(animals.count('lion'))

#set is unordered but no duplicate entries are present
#set does not have any indexes we cannot access by index
set = {10,20,30,10,'lion'}
print(set)

#range is iterating two values
range(10)
print(range)

print(list(range(11)))

#list can have dictionary , tuples, set
a = {1,2,3,4,5}
b = {4,5,6,7,8}
c = [a,b]
print(c)