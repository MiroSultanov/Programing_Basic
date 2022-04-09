# Write a console program that reads the age (real number) and gender ('m' or 'f') entered by the user and prints an address from the following:
# ⦁ "Mr." - male (gender 'm') aged 16 or over
# ⦁ "Master" - a boy (gender 'm') under 16 years
# ⦁ "Ms." - a woman (gender 'f') aged 16 or over
# "" Miss "- a girl (gender 'f') under 16 years

# Sample input and output
# input Output
# 12f  Miss
# 17m  Mr.
# 25f  Ms.
# 13.5m  Master

age = float(input())
gender = input()
if gender == 'm':
    if age < 16:
        print("Master")
    else:
        print("Mr.")
elif gender == 'f':
    if age < 16:
        print('Miss')
    else:
        print("Ms.")
