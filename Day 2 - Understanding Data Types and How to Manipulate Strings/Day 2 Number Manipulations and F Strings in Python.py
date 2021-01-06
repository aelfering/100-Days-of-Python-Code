#   it is super easy to round numbers in Python

print(round(8/3))
print(round(8 / 3, 2))  #   2 for the number of decimal places 



#   floor expression will print a result into an integer...even if it is a clean integer
print(8 // 3)



#   what if you want to divide a number, then divide it again?
result = 4/2
result /= 2 #   divides the result variable by 2 again

print(result)



#   hypothetical example in a game
score = 0
#   if the user scores a point
score += 1

#   that way you do not have to rewrite the same variable over and over


#   there is also f-string that mix different data types

#   here is what we have to do right now
print("your score is " + str(score))

#   BUT we could do this instead 
score = 0
height = 1.8
isWinning = True 

print(f"your score is {score}, your height is {height}, and {isWinning}")

#   this cuts down the amount of code needed



####    CODING CHALLENGE
#   your life in weeks

#   create a program using math and f-strings that tells us how many days, weeks, and months
#       we have left to live until we are 90 years old
#   it should fit the sentence:
#       "You have x days, y weeks, and z months left"

age = int(input("what is your current age?\n"))
days = age * 365
months = days/30
weeks = days/7

target_age = 90
target_days = target_age * 365
target_months = target_days/30
target_weeks = target_days/7

years_left = round(target_age-age, 1)
days_left = round(target_days-days, 1)
months_left = round(target_months-months, 1)
weeks_left = round(target_weeks-weeks, 1)

print(f"You have roughly {days_left} days, {weeks_left} weeks, {months_left} months, and {years_left} years left until you are {target_age} years old.")





















