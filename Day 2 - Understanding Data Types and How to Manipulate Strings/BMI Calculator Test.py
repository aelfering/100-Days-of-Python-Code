height = input("Enter your height in meters:\n")
weight = input("Enter your weight in kilograms:\n")

heightint = float(height)
weightint = float(weight)

bmi = weightint/(heightint ** 2)

print(bmi)