#   mathematical operations you can use in Python

subtraction = 3-7
addition = 3 + 7
multiplication = 3 * 7
division = 3/7

#   division ALWAYS ends in a decimal

print(type(3/7))


exponent = 2**2


#   order of operations matter
#   PEMDAS LR
#       Parentheses         ()
#       Exponents           **

#       Multiplication      *
#       Division            /

#       Addition            +
#       Subtraction         -

#       LEFT
#       RIGHT

#   multiplication and division are equally important...whichever is furthest to the left goes first

print(3 * 3 + 3 / 3 - 3)

#   the result should be 7

#   if you wanted your answer to be 3...
print(3 * (3 + 3) / 3 - 3)

#   add parentheses to the '3 + 3' expression










####    CODING CHALLENGE
#   write a program that calculates the body mass index (BMI) from a user's height and weight

#   BMI = weight(kg) / height**2(m**2)

height = input("Enter your height in meters:\n")
weight = input("Enter your weight in kilograms:\n")

heightint = float(height)
weightint = float(weight)

bmi = weightint/(heightint ** 2)

print(bmi)































