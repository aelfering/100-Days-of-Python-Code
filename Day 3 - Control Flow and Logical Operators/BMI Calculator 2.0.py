#BMI Calculator 2.0

height = float(input("enter your height in m:\n"))
weight = float(input("enter your weight in kg:\n"))

#the formula for BMI is height/weight ** 2

bmi_calc = round(weight/height ** 2)

if bmi_calc < 18.5:
    print(f"Your BMI is {bmi_calc}. You are underweight")
elif bmi_calc >= 18.5 and bmi_calc < 25:
    print(f"Your BMI is {bmi_calc}. You have a normal weight")
elif bmi_calc >= 25 and bmi_calc < 30:
    print(f"Your BMI is {bmi_calc}. You are overweight")
elif bmi_calc >= 30 and bmi_calc < 35:
    print(f"Your BMI is {bmi_calc}. You are obese")
else:
    print(f"Your BMI is {bmi_calc}. You are clinically obese")