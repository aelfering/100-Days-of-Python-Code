####    PYTHON VARIABLES    ####

input("What is your name?")
#   there is no way (yet) to refer to the input to this prompt


#   variables!
name = input("What is your name?")
#   the answer to this input is stored in the variable name

nameperson = 'Alex Elfering'
print(nameperson)

nameperson = 'Zach Simms'
print(nameperson)

#   make sure to not overwrite variable names if you don't want that

namequestion = input('What is your name?')
print(len(namequestion))

####    CODING CHALLENGE 4  ####
a = input("a: ")
b = input("b: ")

#   how do you switch the contents of a and b without rewriting the code?
c = a
a = b
b = c

print("a = " + a)
print("b = " + b)


#   what are the rules of naming variables?
#       make the code readable!
#       numbers are only allowed after a character 
#       good practice not to use function names as variable names
#       make sure to spell variable names correctly 
