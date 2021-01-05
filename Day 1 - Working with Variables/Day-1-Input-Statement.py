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
