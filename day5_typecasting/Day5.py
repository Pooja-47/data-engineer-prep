""" Typecasting:-
The conversion of one datatype to another.
There are various methods in python for typecasting:
int() float() str() tuple() list() dict() ord() hex() set() oct() etc..
Conversion works only if the value is valid for that data type"""
print()
a="1"
b="2"
# Here a and b are strings
print(a+b) # returns 12
print(int(a)+int(b)) # first convert a and b to integers. (returns 3)

# Two types of typecasting or type conversion:
print()
# 1. Explicit Conversion (The programmer tells interpreter to convert)
string="15"
number=7
string_number=int(string) # Shows error if string is not valid integer
result = number + string_number
print("The sum of both the numbers is:",result)

# print(int("abc"))   This will give an error

# 2. Implicit Conversion (The interpreter does itself)
print()
x=9
y=8.0
z = x + y # converts x to float to perform operation
print(z) # shows result in float (prevents data loss)





