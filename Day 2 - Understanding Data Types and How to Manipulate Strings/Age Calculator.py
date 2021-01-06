age = int(input("what is your current age?\n"))
days = age * 365
months = days/31
weeks = days/7

years_left = round(90-age, 1)
days_left = round(years_left * 365)
months_left = round(years_left * 12)
weeks_left = round(years_left * 52)

print(f"You have roughly {days_left} days, {weeks_left} weeks, {months_left} months, and {years_left} years left until you are 90 years old.")