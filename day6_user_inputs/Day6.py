""" Taking User Input:
       We can take user input directly using input() function.
       input() returns data as string by default
       We need to typecast whenever required, for datatypes other than string"""

print()
a=input()
print("The input is:",a) # prints the value user gives at run time.
print()

x=input("Enter first Number:")
y=input("Enter second Number:")
print("The sum is:",x+y) # returns output as string concatenation.
print()

# Typecasting in user input

a1=input("Enter Number1:")
a2=input("Enter Number2:")
print("The sum is:",int(a1)+int(a2)) # returns integer answer

print()

# Another way

X=int(input("Enter any integer num:")) # input is directly converted to integer
print(X)

Y=float(input("Enter any number:")) 
print(Y)
print()

#Arithmetic calculations:

b1=input("Enter value of b1:")
b2=input("Enter value of b2:")
print("The sum is:",b1+b2)

## These will give error because operations are not supported between strings
# print("The difference is:",b1-b2)  
# print("The product is:",b1*b2)  
# print("The division is:",b1/b2) 
print()
print("After typecasting:")
print("The sum is:",int(b1)+int(b2))
print("The difference is:",int(b1)-int(b2))  
print("The product is:",int(b1)*int(b2))
print("The division is:",float(b1)/float(b2)) 

 