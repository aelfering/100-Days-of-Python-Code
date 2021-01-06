# FINAL PROJECT: The Tip Calculator

print("Welcome to the tip calculator")

total_bill = float(input("What was the total bill?\n"))
total_tip = float(input("What percentage tip would you like to give? 10, 12, or 15?\n"))
total_split = int(input("How many people are splitting the bill?\n"))

total_to_pay = "{:.2f}".format((total_bill + (total_bill*(total_tip/100)))/total_split)

#print(total_to_pay)

print(f"Each person should pay: ${total_to_pay}")