#   An else if statement is a form of conditional code

#   sample
#if condition:
#    do this
#else:
#    do this
    
#water_level = 50
#if water_level > 50:
#        print("Drain the water")
#else:
#        print("Keep filling with water")



print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm?\n"))

#spacing and identation matters A LOT in Python
if height > 120:
    print("You can ride the rollercoaster")
else:
    print("Sorry, you are too short to ride the rollercoaster")
    
#   mind your comparison operators
#   ==      equal to    
#   >       greater than
#   <       less than
#   >=      greater than/equal to
#   <=      less than/equal to
#   !=      not equal to


#   CODING CHALLENGE
#   create a script that identifies if a number is odd or even (or prime?)

#   introducing the MODULO operation

remainder_of_division = 7 % 2    

test_number = int(input("What is your number?"))

modulo_ouput = test_number % 2

if modulo_ouput == 0:
    print("Your number is even")
else:
    print("Your number is odd")
    
    
    
    
    
    
    
    