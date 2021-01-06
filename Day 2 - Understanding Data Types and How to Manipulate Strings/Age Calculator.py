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