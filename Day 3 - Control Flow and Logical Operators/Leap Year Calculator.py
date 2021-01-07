# Leap Year Calculation

year = int(input("Which year do you want to check?"))

divis_4 = year % 4
divis_100 = year % 100
divis_400 = year % 400

# if the year is divisible by 400, not by 100, but also divisible by 4

if divis_4 == 0:
    if divis_100 == 0:
        if divis_400 == 0:
            print('Leap Year')
        else:
            print('Not a leap year.')
    else:
        print("Leap year.")
else:
    print("Not a leap year.")
    
    