#Comments, Escape sequence, Print in Python:
 #Comments:
print()
print("Hello Pooja, welcome to the journey of learning Python.")
print(33*14)

# print() it prints output on screen- this is a comment (single line comment).

"""We use comments to explain a specific block of code.
For multiple line comments we can also use ''' ''''
--this is multiple line comment."""

'''Comments are not executed by interpreter.
interpreter ignores comments.'''

#Escape Sequence Characters:

"""print("Hello
      Pooja") 
Above print gives error.
In this way can't print hello and pooja in diff lines.
So in such situations we use Escape Sequence Characters"""
print()
print("Hello Pooja \nYou are Welcome")
#Here \n is an ESC(Escape Sequence Character) for new line.

print("Hello \"Pooja\"")
#Here \" is an ESC similarly \' is also an ESC.

'''We use ESCs to insert characters that cannot be directly used in string.'''

#Parameters of print:
 #Multiple values-
print()
print("Pooja",110,"CS",79)

#Separater- separates multiple values by given symbol(default space).
print("Pooja",110,"CS",79,sep="~")

#end- prints the given symbol at the end of line it can be null.
print("Pooja",110,"CS",79, end="end")
print("Student")
print()
print("Pooja",110,"CS",79, end="999")
print("Student")
print()
print("Pooja",110,"CS",79, end="01\n")
print("student")






 