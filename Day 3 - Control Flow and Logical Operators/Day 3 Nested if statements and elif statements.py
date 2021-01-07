#   the standard if else statement looks like this

if condition:
    do this
else:
    do this
    
#   BUT what about a nested statement?    

if condition:
    if another condition:
    #   for this to happen, then both if statements must be true
        do this
    else:
        do this
else:
    do this
    
#   expanding on the last exercise...

print("Welcome to the rollercoaster")
height = int(input("What is your height in centimeters?\n"))

if height >= 120:
    print("You can ride the rollercoaster!")
    age = int(input("What is your age?\n"))
    if age >= 12 and age <= 18:
        print("Please pay $7.")
    #the elif statement allows you to add as many conditions as you would like
    elif age < 12:
        print("Please pay $5.")
    else:
        print("Please pay $12.")
else:
    print("Sorry, you cannot ride the rollercoaster")
