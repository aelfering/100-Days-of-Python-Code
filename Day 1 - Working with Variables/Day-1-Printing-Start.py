#   the print() funtion will return whatever is in the parentheses
#   the quotation marks identify a string

print("hello world!")

#   don't forget to close out the quotation marks or parentheses, otherwise a syntax error
#   you can always copy and paste the error message into Google to usually pull up StackOverFlow

#   the color of your code will help guide your script if something is wrong



####   CODING CHALLENGE #1  ####
print('what to print')

#   this should print the string "what to print"

print("print('what to print')")

#   if you are using quotes within quotes then use double quotes on the outside AND single quotes on the bottom 








####    STRING MANIPULATION ####
#   to write on a new line within a string when printing, use \n

print("Hello world\nHello world\nHello world\nHello world")

#   this saves lines

#   we can also concatenate strings together 

print("Hello" + " " + "Alex Elfering")

#   spaces matter when using python! Mind indentation errors

####    CODING CHALLENGE 2  ####

#   How to debug code by each line

print(Day - 1 String Manipulation")
#   quotation marks are missing at the beginning of the string. Python thinks everything before the quote is code
#   solution:
print("Day 1 - String Manipulation")

print("String concatenation is done with the "+" sign.")
#   this is correct, but I think they want to include the plus sign
#   solution:
print("String concatenation is done with the + sign.")

    print('e.g. print("Hello " + "world")')
#   indentation error
#   solution
print("e.g. print('Hello ' + 'world')")    

print(("New lines can be created with a backslash and n.")
#   too many parentheses on the left-hand side
#   solution:
print("New lines can be created with a backslash and n.")










####    Python Input Statement  ####

print("Hello" + " " + "Alex Elfering")

#   what if we want to input data?

input("a prompt for the user")
input("What is your name?")
#   the script will then prompt you with this question followed by a cursor ready for data entry. If you answer it with a string, then it is returned in the prompt

print("Hello, " + input("What is your name?"))
#   here we have a nested statement
#   The script will prompt you for your name. If you enter a string, then the script will respond "Hello ___ "

#   thonny.org is a good resource to utilize



####    coding challenge 3  ####

#   idea: if a user types in their name, the script should return the length of their name

#   len() is the length of the string

print(len(input("What is your name?")))

#   first you create your input statement
#   then you use the len() function to wrap the input 
#   lastly print the results











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



























































































