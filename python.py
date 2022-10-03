#..w3schools..#



print("hello world")

if 5 > 2:
  print("Five is greater than two!")

x = 5
y = "Hello, World!"

#This is a comment.

"""
This is a comment
written in
more than just one line
"""

x = 5
y = "John"
print(x)
print(y)

x = 4       # x is of type int
x = "Sally" # x is now of type str
print(x)

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

x = 5
y = "John"
print(type(x)) #<class 'int'>
print(type(y)) #<class 'str'>

#variable name cannot start with a number(Only A-z, 0-9, and _ )

x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x) #apple
print(y) #banana
print(z) #cherry

x = "Python"
y = "is"
z = "awesome"
print(x, y, z) #OR print(x + y + z)

x = 5
y = "John"
print(x, y) #5 John
#print(x + y) = ERROR

#Global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

#Local variables
x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) #Python is fantastic

myfunc()

print("Python is " + x) #Python is awesome

#Global keyword
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #Python is fantastic

#Change variable via global keyword
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x) #Python is fantastic

#Data Types @@@@@Refresh@@@@
'''
Text Type:	str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	NoneType
'''
x = 5
print(type(x)) #<class 'int'>

x = 1    # int
y = 2.8  # float (Note: y = 35e3 is float)
z = 3 + 1j   # complex

#Type Conversion
a = float(x) # 1.0
b = int(y) #2
c = complex(x) #1 + 0j

print(type(a)) #<class 'float'>
print(type(b)) #<class 'int'>
print(type(c)) #<class 'complex'>



















