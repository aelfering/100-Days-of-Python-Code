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