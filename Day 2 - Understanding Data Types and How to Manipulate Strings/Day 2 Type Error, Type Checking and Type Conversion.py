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






#   CODING CHALLENGE    
#   write a program that adds the digits in a two digit numbers
#       if the number is 35, then the output should be 3 + 5 = 8

39

#   the output should be 3 + 9 = 12

number = input("Type a two digit number\n")
print(int(number[0]) + int(number[1]))

#   the video solution was

first_digit = number[0]
second_digit = number[1]

print(type(first_digit))

result = int(first_digit) + int(second_digit)
print(result)





























