#   when you use a function, you take an input and expect an output

#   when you pass a rock through a french fry machine, it breaks

num_char = len(input("What is your name?"))
print("Your name has " + num_char + " characters.")

#   THIS breaks because a string on line 6 is expected

#   tells you what the data type is (this is an integer)
print(type(num_char))


#   We can also type convert or cast

new_num_char = str(num_char)
#   this converts to a string

num_char = len(input("What is your name?"))
print("Your name has " + new_num_char + " characters.")


a = float(123)
print(type(a))


#   this adds numbers together 
print(2 + 4)

#   this concatenates
print("2" + "4")